from run import app
from flask import render_template,request,redirect

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')