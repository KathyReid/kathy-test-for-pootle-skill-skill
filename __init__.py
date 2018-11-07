from mycroft import MycroftSkill, intent_file_handler


class KathyTestForPootleSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.pootle.for.test.kathy.intent')
    def handle_skill_pootle_for_test_kathy(self, message):
        self.speak_dialog('skill.pootle.for.test.kathy')


def create_skill():
    return KathyTestForPootleSkill()

