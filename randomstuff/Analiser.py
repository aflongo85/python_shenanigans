
class Analiser:

    def ig_analysis(self, start_date, end_date, number_of_posts):
        number_of_days = (end_date - start_date).days
        print("First photo was posted on {} which means {} years ago".format(start_date, number_of_days / 30 / 12))
        print("Number of days since first post = {} Number of posts = {}".format(number_of_days, number_of_posts))
        print("Average posts per day = {}".format(number_of_posts / number_of_days))