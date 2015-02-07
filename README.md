MyBlog
=======
### if you need to run the test directly, you can export PYTHONPATH to this directory first
### you can use the provided virtualenv for mac to run it

### run db migrate
in src folder
``` 
python manage.py db init
```
在使用上面的语句后会在env.py中生成
```
from flask import current_app
config.set_main_option('sqlalchemy.url', current_app.config.get('SQLALCHEMY_DATABASE_URI'))
target_metadata = current_app.extensions['migrate'].db.metadata
```
这样会对metadata进行绑定,在之后定义model时继承自db.Model即可动态model的变化

执行`python manage.py db migrate`只会生成alembic_version表,执行`python manage.py db upgrade`才会按照生成的迁移文件进行表的migrate