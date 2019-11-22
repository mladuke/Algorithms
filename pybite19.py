from datetime import datetime,timedelta

NOW = datetime.now()

class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires
    
    @property
    def expired(self):
        status = False
        if self.expires < datetime.now() :
            status = True
        return status

''' class Promo:

    def __init__(self, name, expires=NOW):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return datetime.now() > self.expires '''


def test_promo_expired():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    assert twitter_promo.expired


def test_promo_not_expired():
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    assert not newsletter_promo.expired

test_promo_expired()
test_promo_not_expired()