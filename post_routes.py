from shared_resources import *


@app.route('/posts', methods=['POST', 'GET'])
def create_and_get_all_posts():
    if request.method == 'POST':
        content = request.get_json()
        new_post = datastore.entity.Entity(key=client.key(POSTS))
        new_post.update({
            "title": content.get("title", ""),
            "description": content.get("description", ""),
            "post-type": content.get("post-type", ""),
            "url": content.get("url", ""),
            "created_at": datetime.utcnow()
            # add image later
        })
        client.put(new_post)
        post_id = new_post.key.id
        redirect_url = f"https://sodasofa.art/posts/{post_id}"
        new_post.update({"self": redirect_url})
        client.put(new_post)
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
    post_key = client.key(POSTS, post_id)
    post = client.get(key=post_key)

    if post is None:
        return jsonify(error="Post does not exist"), 404

    if request.method == 'GET':
        post['id'] = post.key.id
        return render_template('post.j2', post=post)

    elif request.method == 'DELETE':
        try:
            client.delete(post_key)
            return jsonify(message="Post deleted", success=True), 200

        except Exception as e:
            logging.error(f"Failed to delete course: {str(e)}")
            return jsonify(error="Failed to delete course"), 500
