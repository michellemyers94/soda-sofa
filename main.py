from shared_resources import *
import post_routes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    # Create a Cloud Datastore client.
    datastore_client = datastore.Client()

    # Use the Cloud Datastore client to fetch all entities of the kind 'posts'.
    query = datastore_client.query(kind='posts')
    posts = list(query.fetch())

    # Render your template with the posts.
    return render_template('dashboard.j2', posts=posts)


@app.route('/upload')
def upload():
    return render_template('upload.j2')


@app.route('/my-uploads')
def my_uploads():
    query = client.query(kind='posts')
    results = list(query.fetch())
    posts = []
    for post in results:
        posts.append({
            'title': post['title'],
            'description': post['description'],
            'post-type': post['post-type'],
            'created_at': post['created_at'],
            'self': post['self']
        })

    return render_template('my-uploads.j2', posts=posts)


@app.route('/all-uploads')
def all_uploads():
    # Create a Cloud Datastore client.
    datastore_client = datastore.Client()

    # Use the Cloud Datastore client to fetch all entities of the kind 'posts'.
    query = datastore_client.query(kind='posts')
    posts = list(query.fetch())

    # Render your template with the posts.
    return render_template('all-uploads.j2', posts=posts)


# Search for POSTS
@app.route('/posts/search' , methods=['GET'])
def search_posts():
    keyword = request.args.get('keyword', '').lower()

    query = client.query(kind=POSTS)

    posts = list(query.fetch())

    filtered_posts = [post for post in posts if keyword in post['description'].lower() or keyword in post['title'].lower()]

    for post in filtered_posts:
        post['id'] = post.key.id

    return jsonify(filtered_posts)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
