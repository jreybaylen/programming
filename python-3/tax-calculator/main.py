from classes.profile import Profile

def atm_init():
    profile = Profile()
    
    profile.get_information()
    profile.display_information()
    profile.compute_tax('yearly')
    profile.take_home()

atm_init()