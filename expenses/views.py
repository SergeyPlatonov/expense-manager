from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import CATEGORY_CHOICES, Expense
from .forms import (
    ExpenseForm,
    RegisterForm,
    LoginForm,
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Sum


# Create your views here.
@csrf_protect
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "expenses/register.html", {"form": form})


@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "expenses/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    month = request.GET.get("month")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    category = request.GET.get("category")
    if month:
        year, month_num = map(int, month.split("-"))
        expenses = expenses.filter(date__year=year, date__month=month_num)
    if start_date and end_date:
        expenses = expenses.filter(date__range=[start_date, end_date])
    if category:
        expenses = expenses.filter(category=category)
    expenses = expenses.order_by("-date", "-time")
    paginator = Paginator(expenses, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    daily_totals = expenses.values("date").annotate(total=Sum("amount")).order_by("date")
    category_totals = expenses.values("category").annotate(total=Sum("amount")).order_by("category")
    categories = CATEGORY_CHOICES
    return render(
        request,
        "expenses/dashboard.html",
        {
            "page_obj": page_obj,
            "daily_totals": list(daily_totals),
            "category_totals": list(category_totals),
            "month": month,
            "start_date": start_date,
            "end_date": end_date,
            "category": category,
            "categories": categories,
        },
    )


@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, "Expense record added!")
            return redirect("dashboard")
    else:
        form = ExpenseForm()
    return render(request, "expenses/add_expense.html", {"form": form})


@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense record updated!")
            return redirect("dashboard")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "expenses/edit_expense.html", {"form": form, "expense": expense})


@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        expense.delete()
        messages.success(request, "Expense record deleted!")
        return redirect("dashboard")
    return render(request, "expenses/delete_expense.html", {"expense": expense})


@login_required
def password_change(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password changed successfully!")
            return redirect("dashboard")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, "expenses/password_change.html", {"form": form})


@csrf_protect
def password_reset_request(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name="expenses/password_reset_email.html",
                subject_template_name="expenses/password_reset_subject.txt",
            )
            messages.success(request, "Password reset email sent!")
            return redirect("login")
    else:
        form = CustomPasswordResetForm()
    return render(request, "expenses/password_reset.html", {"form": form})


@csrf_protect
def password_reset_confirm(request, uidb64, token):
    return PasswordResetConfirmView.as_view(
        template_name="expenses/password_reset_confirm.html", form_class=CustomSetPasswordForm
    )(request, uidb64=uidb64, token=token)
