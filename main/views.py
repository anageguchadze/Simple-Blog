from django.shortcuts import render

# Create your views here.
def main_view(request):
    return render(request, 'index.html')

def blog_view(request):
    blogs = [
        {'title': 'Capturing Moments', 'description': 'The Art and Science of Photography in the Digital Age', 'author': 'Lena Caldwell'},
        {'title': 'The Evolution of Photography', 'description': 'From Film to Digital and Beyond', 'author': 'Owen Ramsey'},
        {'title': 'Mastering the Perfect Shot', 'description': 'Essential Tips for Aspiring Photographers', 'author': 'Amelia Townsend'},
        {'title': 'The Impact of Photography on Social Media', 'description': 'How Images Shape Our Online Presence', 'author': 'Ethan McAllister'},
        {'title': 'Exploring the World Through a Lens', 'description': 'The Importance of Photography in Storytelling', 'author': 'Sophia Whitman'},
    ]

    return render(request, 'blog.html', {'blogs': blogs})