# from django.shortcuts import render, redirect, get_object_or_404
# from .models import TODO
# from . forms import TodoForms
# from django.contrib.auth.decorators import login_required
# from rest_framework import generics, permissions      
# from .serializer import TodoSerializer


# # BL- decorator to ensure only logged-in users can access this view
# @login_required
# def todo_list(request):
#     # 1. Get the data (The Query)
#     todos = TODO.objects.filter(owner=request.user)
    
#     # 2. Pack the data
#     context = {
#         'todos': todos
#     }
    
#     # 3. Return the webpage with the data
#     return render(request, 'todos/todo_list.html', context)

# @login_required
# def todo_create(request):
#     if request.method == 'POST':
#         form = TodoForms(request.POST)
#         if form.is_valid():
#             todo = form.save(commit=False)
#             todo.owner = request.user
#             todo.save()
#             return redirect('todo_list')
#     else:
#         form = TodoForms()
#     return render(request, 'todos/todo_form.html', {'form': form})

# @login_required
# def todo_update(request, pk):
#     todo = get_object_or_404(TODO, pk = pk, owner = request.user)

#     if request.method == 'POST':
#         form = TodoForms(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoForms(instance=todo)
#     return render(request, 'todos/todo_form.html', {'form': form})


# @login_required
# def todo_delete(request, pk):
#     todo = get_object_or_404(TODO, pk=pk, owner=request.user)
    
#     if request.method == 'POST':
#         # Your code here: Delete the todo and redirect to 'todo_list'
#         todo.delete()
#         return redirect('todo_list')
        
        
#     # If it's a GET request, we show the confirmation page
#     return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})


# class TodoListAPI(generics.ListCreateAPIView):
#     queryset = TODO.objects.all()
#     serializer_class = TodoSerializer

# # class TodoListAPI(generics.ListCreateAPIView):
# #     serializer_class = TodoSerializer
# #     permission_classes = [permissions.AllowAny] # 1. Lock the door
# #     # permission_classes = [permissions.IsAuthenticated] # 1. Lock the door

# #     # 2. Filter: Only show my own tasks
# #     def get_queryset(self):
# #         return TODO.objects.filter(owner=self.request.user)

# #     # 3. Create: Auto-assign the owner when saving
# #     def perform_create(self, serializer):
# #         serializer.save(owner=self.request.user)

# class TodoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TODO.objects.all() # 👈 match your model class name
#     serializer_class = TodoSerializer

# # class TodoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
# #     serializer_class = TodoSerializer
# #     # permission_classes = [permissions.IsAuthenticated]
# #     permission_classes = [permissions.AllowAny]

# #     # Ensure we only search within the user's tasks
# #     def get_queryset(self):
# #         return TODO.objects.filter(owner=self.request.user)





from rest_framework import generics, permissions
from .serializer import TodoSerializer
from .models import TODO
from django.contrib.auth.models import User  # 👈 1. New Import

class TodoListAPI(generics.ListCreateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]

    # 👈 2. Add this method
    def perform_create(self, serializer):
        # Assign the task to the first user in the database (Admin)
        # This prevents the "Owner cannot be null" error
        user = User.objects.first() 
        serializer.save(owner=user)

class TodoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]


