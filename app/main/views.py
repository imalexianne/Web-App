from flask_login import login_required,current_user
from . import main
from flask import render_template,request,redirect,url_for,abort
# from ..models import User,PhotoProfile
from ..models import User,Pitch
from .forms import UpdateProfile,PitchForm
# from .forms import ReviewForm,UpdateProfile
from .. import db,photos
import markdown2 



# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    all_pitches = Pitch.get_pitches
    

    title = 'Home - Welcome to The best Pitches Online'

    return render_template('index.html', title = title, all_pitches = all_pitches )



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


# @login_required
# def new_review(id):

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    
    if form.validate_on_submit():
        # title = form.title.data
        description_path = form.description_path.data
        category = form.category.data
        # Updated review instance
        new_pitch = Pitch(description_path=description_path, category=category, user_id= current_user.id)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.index',description_path = description_path ))

    # title = f'{movie.title} review'
    return render_template('new_pitch.html', pitch_form=form)





@main.route('/pitch/<int:id>')
def single_pitch(id):
    login_required
    pitch=Pitch.query.get(id)
    if pitch is None:
        abort(404)
    format_pitch = markdown2.markdown(pitch.user_pitch,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('pitch.html',pitch = pitch,format_pitch=format_pitch)



@main.route('/pitch')
def diplay_pitch():
   all_pitches = Pitch.get_pitches()
   print(all_pitches)
   return render_template("pitch.html",all_pitches = all_pitches)