from shared_resources import *
import post_routes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    try:
        user_timezone = 'America/Los_Angeles'
        response = requests.get('https://sodasofa.art/posts')
        if response.status_code == 200:
            data = response.json()
            posts = data['posts']
            for post in posts:
                created_at = post.get('created_at')
                if created_at:
                    try:
                        dt_obj_utc = datetime.strptime(created_at, "%a, %d %b %Y %H:%M:%S GMT")
                        dt_obj_utc = dt_obj_utc.replace(tzinfo=pytz.utc)
                        user_tz = pytz.timezone(user_timezone)
                        local_dt = dt_obj_utc.astimezone(user_tz)
                        post['created_at'] = local_dt.strftime(
                            '%Y-%m-%d %I:%M:%S %p')  # Example format: '2024-01-01 08:30:00 PM'
                    except ValueError as ve:
                        app.logger.error(f"Date formatting error for post {post['id']} with created_at = '{created_at}': {ve}")
                        post['created_at'] = ''
                else:
                    post['created_at'] = ''
    except requests.exceptions.RequestException as e:
        return jsonify(error='An error occurred during the request'), 500
    return render_template('dashboard.j2', posts=posts)


@app.route('/upload')
def upload():
    return render_template('upload.j2')


# CRUD for POSTS


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
