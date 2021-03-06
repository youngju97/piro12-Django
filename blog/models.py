from django.db import models

class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=80)
    content = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    upgraded_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    massage = models.TextField()

    """
        on_delete : Commnet는 Post에 속해있는 잖아.
        그러면 속해있는 부모인 Post가 삭제되면 그거에 딸린 Comment들은 어쩔건지
        CASCADE : Post 삭제되면 관련 comment도 다 삭제하겠다.
        """

