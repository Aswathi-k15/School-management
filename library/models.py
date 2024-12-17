

from django.db import models
from students.models import Student # type: ignore

class LibraryHistory(models.Model):
    student_id= models.ForeignKey(Student, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.book_name} - {self.student.name}"