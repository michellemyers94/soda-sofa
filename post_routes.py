from shared_resources import *


@app.route('/posts', methods=['POST', 'GET'])
def create_and_get_all_posts():
    if request.method == 'POST':
        content = request.get_json()
        new_post = datastore.entity.Entity(key=client.key(POSTS))
        new_post.update({
            "title": content["title"],
            "description": content["description"],
            "post-type": content["post-type"],
            "url": content["url"],
            "created_at": datetime.utcnow()
            # add image later
        })
        client.put(new_post)
        post_id = new_post.key.id
        new_post.update({"self": f"https://sodasofa.art/posts/{post_id}"})
        client.put(new_post)
        return jsonify({"id": post_id}), 201

    elif request.method == 'GET':
        query = client.query(kind=POSTS)
        posts = list(query.fetch())
        response = {
            'posts': posts
        }

        return jsonify(response), 200
    else:
        return jsonify({"error": "Method not recognized"})
