from plone.app.contentrules.handlers import execute, is_portal_factory
from Acquisition import aq_inner


def execute_rules(event):
    """ When an action is invoked on an object,
        execute rules assigned to its parent.
        Base action executor handler """

    if is_portal_factory(event.object):
        return

    execute(aq_inner(event.object), event)
