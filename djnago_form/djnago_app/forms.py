from django import forms


class Feedback(forms.Form):
    name = forms.CharField(max_length = 20)
    roll = forms.IntegerField()
    email = forms.EmailField()
    comments = forms.CharField(widget = forms.Textarea)
    #form validation
    def clean_name(self):
        n = self.cleaned_data['name']
        if len(n) > 10:
            raise forms.ValidationError("length of name field must be < 10")
            return n
    def clean_roll(self):
        r = self.cleaned_data['roll']
        r1 = str(r)
        if len(r1) > 4:
            raise forms.ValidationError("length of roll field must be < 4")
            return r1
