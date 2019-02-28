from app.models import Pitch,User
from app import db


def setUp(self):
        self.user_wecode = User(username = 'wecode',password = 'alexianne', email = 'imalexianne@gmail.com')
        self.new_pitch = Pitch(user_id=user_id,,image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",user_pitch='This movie is the best thing since sliced bread',user = self.user_wecode )

def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.user_id,12345)
        # self.assertEquals(self.new_pitch.movie_title,'Review for movies')
        self.assertEquals(self.new_pitch.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_pitch.user_pitch,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_pitch.user,self.user_wecode)


def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(pitch.query.all())>0)


def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        got_pitches = pitch.get_pitches(12345)
        self.assertTrue(len(got_pitches) == 1)