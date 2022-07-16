class UserService:
    @classmethod
    def update_user(cls, user, data):
        user.name = data.get('name')
        user.phone = data.get('phone')
        user.birthday = data.get('birthday')
        user.email = data.get('email')
        user.gender = data.get('gender')
        user.career = data.get('career')
        user.save()
        return user
