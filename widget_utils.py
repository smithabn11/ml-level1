from IPython.display import display
import ipywidgets as widgets
import os


REPO_PATH = ''

def machine_learning():
    display(widgets.HTML(value="<b> Does Machine learning </b> <i>always</i> <b>require output accompanying the data to learn ? </b> <br> Click the below button to choose your answer"))
    yes = widgets.Button(description='Yes')
    display(yes)
    no = widgets.Button(description='No')
    display(no)
    answer_html_yesno = widgets.HTML(value="")
    answer_box=widgets.Box([answer_html_yesno])
    display(answer_box)
    def yes_learning(b):
        b.disabled = True
        answer_html_yesno.value = "<b>Answer: Not Really (You clicked on Yes) </b> <p> There are Machine learning programs which can " +\
                                   "learn useful information from the data without output. <i> It's called Unsupervised Learning. </i> </p>" +\
                                   "The Machine learning programs which can learn from dataset and output  " +\
                                   "are called <i> Supervised learning. </i> We are going to explore Supervised learning in this lab. </p>"+\
                                   "<p> To learn more about Unsupervised learning go to Unsupervised learning Machine Learning Village lab </p>"

    def no_learning(b):
        b.disabled = True
        answer_html_yesno.value = "<b>Answer: Correct (You clicked on No) </b> <p> The Machine learning programs which can learn from " + \
                                   "output are called <i> Supervised learning. We are going to explore Supervised learning in this lab. </i></p>" +\
                                   "There are Machine learning programs which can learn useful information from dataset without output." +\
                                   "</b> <i> It's called Unsupervised Learning. </i>" +\
                                   "<p> To learn more about Unsupervised learning go to Unsupervised learning Machine Learning Village lab </p>"

    yes.on_click(yes_learning)
    no.on_click(no_learning)


def feature_selection():
    display(widgets.HTML(
        value="<b> Click on a below button to select a good feature to distinguish between green apples vs oranges </b> <br> Click the below button to choose your answer"
    ))

    feature_shape = widgets.Button(description='shape')
    display(feature_shape)
    feature_weight = widgets.Button(description='weight')
    display(feature_weight)
    feature_color = widgets.Button(description='color')
    display(feature_color)
    answer_html = widgets.HTML(value="")
    file = open(os.path.join(REPO_PATH, "images/blank.png"), "rb")
    image = file.read()
    answer_img = widgets.Image(value=image)

    answer_box = widgets.VBox([answer_html, answer_img])
    display(answer_box)

    def on_button_clicked_weight(b):
        b.disabled = True
        answer_html.value = "<b> Answer: Weight is not a good feature to separate. </b> <p>Assume if you are blindfolded and never seen apples nor oranges they weigh similar. Click on other </p>"
        file = open(os.path.join(REPO_PATH, "images/feature_weight.png"), "rb")
        image = file.read()
        answer_img.value = image
        answer_img.format = 'png'
        answer_img.width = 300
        answer_img.height = 300

    def on_button_clicked_shape(b):
        b.disabled = True
        answer_html.value = "<b>Answer: Shape is not a good feature to separate. </b> <p> Apples and oranges are almost round. Click on other </p>"

    def on_button_clicked_color(b):
        b.disabled = True
        answer_html.value = "<b> Answer: Correct. </b> <p> Color is a good feature. You can use color to separate both. One is green other is orange. </p>"
        file = open(os.path.join(REPO_PATH, "images/feature_color.png"), "rb")
        image = file.read()
        answer_img.value = image
        answer_img.format = 'png'
        answer_img.width = 300
        answer_img.height = 300

    feature_weight.on_click(on_button_clicked_weight)
    feature_shape.on_click(on_button_clicked_shape)
    feature_color.on_click(on_button_clicked_color)

def iris_features():
	display(widgets.HTML(value="<b> Click all the features used in this dataset to distinguish different Iris flowers </b> <br> Click the below rows to choose your answer(Multiple values can be selected with shift and/or ctrl (or command) pressed and mouse clicks or arrow keys.)"))
	multiple_items = widgets.SelectMultiple(
	    options=['sepal-length', 'species',  'sepal-width',  'petal-length',  'petal-width'],
	    value=[],
	    description='',
	    disabled=False
	)
	display(multiple_items)


def running():
    MAX_IMAGES_TO_TEST = 1000
    f = widgets.FloatProgress(min=0, max=MAX_IMAGES_TO_TEST, description='Running')
    display(f)
    return f
