from flask import Flask, render_template, session, redirect, url_for, request
app = Flask(__name__)
app.secret_key = 'hXDm8NXqqJATH&7XHW6AtM.XEqM4cEMn'


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    your_name = request.args.get('name', '')
    if your_name:
        # 名前が入力されている場合は、sessionに格納
        session['username'] = your_name
        # todo画面を表示
        return redirect(url_for('todo'))
    else:
        # 名前が未入力の場合は、ログイン画面を再表示
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    # セッションを削除
    session.clear()
    # ログイン画面を表示
    return redirect(url_for('index'))


@app.route('/todo', methods=['POST'])
def todo():
    # ログインしていない場合はログイン画面を表示
    if 'username' not in session:
        return redirect(url_for('index'))

    # タスクが入力されたらセッションに追加
    if request.method == 'POST':
        todo = request.form['todo']
        if todo:
            todo_list = []
            if 'todo' in session:
                todo_list = session['todo']
            todo_list.append(todo)
            session['todo'] = todo_list

    return render_template('todo.html')


@app.route('/todo_clear')
def todo_clear():
    # TODOのセッション情報を削除
    session.pop('todo')
    return redirect(url_for('todo'))


if __name__ == '__main__':
    app.run(debug=True)