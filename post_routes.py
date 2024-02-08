from shared_resources import *

# Define a new function to handle file uploads to avoid clutter in the main function.
def upload_file_to_gcp_storage(file, bucket, filename):
    blob = bucket.blob(filename)
    try:
        blob.upload_from_string(file.read(), content_type=file.content_type)
        return True, f"https://storage.googleapis.com/{bucket_name}/{filename}"
    except Exception as e:
        logging.error("Failed to upload file to GCS: ", exc_info=True)
        return False, f"Failed to upload file: {str(e)}"

@app.route('/posts', methods=['POST', 'GET'])
def create_and_get_all_posts():
    if request.method == 'POST':
        content = request.form
        file = request.files.get('file')
        new_post = datastore.entity.Entity(key=client.key(POSTS))
        new_post.update({
            "title": content.get("title", ""),
            "description": content.get("description", ""),
            "post-type": content.get("post-type", ""),
            "url": content.get("url", ""),
            "created_at": datetime.utcnow()

        })
        client.put(new_post)


        post_id = new_post.key.id
        redirect_url = f"https://sodasofa.art/posts/{post_id}"
        new_post.update({"self": redirect_url})

        # Upload file to GCP Storage if a file is provided
        if file:
            upload_success, response_message = upload_file_to_gcp_storage(file, bucket, secure_filename(file.filename))

            if upload_success:
                # Update the post with the image url
                new_post["image_url"] = response_message
                client.put(new_post)
            else:
                # Return an error response if the upload failed
                return jsonify({"error": response_message}), 500

        client.put(new_post)
        cache.delete_memoized(get_posts)
        get_posts()
        return jsonify({"success": True, "redirectUrl": redirect_url, "id": post_id}), 201

    elif request.method == 'GET':
        query = client.query(kind=POSTS)
        results = list(query.fetch())
        posts = []
        for post in results:
            post_id = post.key.id
            posts.append({
                'id': post_id,
                'title': post['title'],
                'description': post['description'],
                'post-type': post['post-type'],
                'url': post['url'],
                'created_at': post['created_at'],
                'self': post['self']
            })
        response = {
            'posts': posts
        }

        return jsonify(response), 200
    else:
        return jsonify({"error": "Method not recognized"})


@app.route('/posts/<int:post_id>', methods=['GET', 'DELETE'])
def post(post_id: int):
    post = get_post_by_id(post_id)

    if post is None:
        return jsonify(error="Post does not exist"), 404

    if request.method == 'GET':
        return render_template('post.j2', post=post)

    elif request.method == 'DELETE':
        try:
            client.delete(client.key(POSTS, post_id))
            cache.delete_memoized(get_post_by_id, post_id)
            cache.delete_memoized(get_posts)
            return jsonify(message="Post deleted", success=True), 200

        except Exception as e:
            logging.error(f"Failed to delete course: {str(e)}")
            return jsonify(error="Failed to delete course"), 500


@cache.memoize(timeout=50)
def get_posts():
    datastore_client = datastore.Client()
    query = datastore_client.query(kind='posts')
    return list(query.fetch())


@cache.memoize(timeout=50)
def get_post_by_id(post_id: int):
    post_key = client.key(POSTS, post_id)
    post = client.get(key=post_key)

    if post is not None:
        post['id'] = post.key.id

    return post
