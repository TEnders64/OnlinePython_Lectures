# Assignment - Ninja Gold with Leaderboard

### Great job building a bulletproof Login and Registration app!
- You'll be able to use this for nearly every Django project you build!
- Now let's integrate that into a project we've already built to extend it.

Create a new project called `leaderboard`.
- Make a new app called `integration`.
- Copy/paste your Login and Registration app and your Ninja Gold app into the new project's `apps` folder.
- Inside `integration`'s models.py, make a new model called Leaderboard that looks like so:

```python
from ..your_login_reg_app import User

class Leaderboard(models.Model):
	user = models.OneToOneField(User)
	top_score = models.IntegerField()
	games_played = models.IntegerField()
	total_gold_earned = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
```

Now do whatever else is necessary to make it so users have the option of logging in before playing so they can save their scores, and for the top 25 names and scores to be displayed in descending order at `/leaderboard`. Only logged in users can appear on the leaderboard.

Also feel free to modify Ninja Gold to have better gameplay, but remember that the real goal here is to gain fluency at multiple apps and prep for the Belt Reviewer.
