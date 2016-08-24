from system.core.controller import *
import sys

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        courses = self.models['Course'].get_all_courses()
        sys.stderr.write('Test1\n')
        return self.load_view('index.html', courses=courses)

    def add(self):
        sys.stderr.write('Test2\n')
        course_id = self.models['Course'].add_course(request.form)
        sys.stderr.write('Test3\n')
        return redirect('/')

    def confirm_delete(self, id):
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('delete.html', course=course[0])

    def delete(self, id):
        sys.stderr.write(id)
        self.models['Course'].delete_course(id)
        return redirect('/')