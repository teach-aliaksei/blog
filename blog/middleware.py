from blog.models import Category


def my_middle(next):
    def core(request):
        request.session["he"] = 145
        response = next(request)
        response["bye"] = "hek"
        return response
    return core



def categ(request):
    return {"categs": Category.objects.all()}

