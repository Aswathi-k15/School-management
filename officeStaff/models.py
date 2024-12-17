from django.db import models
from school.student.models import Student
from django.contrib.auth.models import User
from school.library.models import LibraryHistory


class FeesHistory(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.student.name} - {self.fee_type}"
    

class Review(models.Model):
    library_record = models.ForeignKey(LibraryHistory, on_delete=models.CASCADE, related_name='reviews')
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)  # The user leaving the review
    rating = models.PositiveSmallIntegerField()  # e.g., 1 to 5 stars
    comment = models.TextField(blank=True, null=True)  # Optional feedback
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Most recent reviews first

    def _str_(self):
        return f"Review by {self.user} - {self.library_record.book_name} ({self.rating}/5)"
