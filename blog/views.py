from django.shortcuts import render

posts = [
    {
        'author': 'Kaustubh',
        'title': 'The Brothers Karamazov - Fyodor Dostoevsky',
        'content': "If there was still any doubt, let me confirm that this actually is the greatest book ever written. But be warned that you need to set aside a solid month to get through it 😵‍💫. And it's not light reading-this is a dense work of philosophy disguised as a simple murder mystery. But it's well worth the effort. It tackles the fundamental question of human existence-how best to live one's life-in a truly engaging way. Dostoevsky created 3 brothers (Ivan, Alexei, and Dmitri) with opposite answers to this fundamental question, and set them loose in the world to see what would happen. A testament to Dostoevsky's genius is he didn't know how the book would evolve when he started writing. As a consequence, the book really isn't about the plot at all, but about how these brothers evolve and deal with their struggles based on their differing world views. Dostoevsky articulates, better than anyone, how human beings really are what I would call 'walking contradictions'. Perhaps all of our struggles in life boil down to the reality that we desire contradictory things, simultaneously. If you like your novels with good character development, this is the masterwork 💙. Dostoevsky's characters are more real, more human, than any other. At different points along the way, you will identify with them, sympathize with them, curse them, agonize over them, celebrate them. You will be moved. Reading this book was a deeply personal experience for me, because I saw myself in one of the characters, and I didn't like what I saw. My worldview, in fact my entire direction in life, shifted as a result of this experience. I can't guarantee the same results for you, but you owe it to yourself to set aside the time, someday, for the Brothers Karamazov. Be sure to read the Pevear Volokhonsky translation.",
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Kaustubh',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})