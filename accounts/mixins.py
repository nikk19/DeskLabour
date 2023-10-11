# from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


# class LabourRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.is_active and self.request.user.is_labour


# class EngineerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.is_active and self.request.user.is_engineer