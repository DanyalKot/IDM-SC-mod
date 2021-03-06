from ..objects import dp, Event, MySignalEvent

@dp.event_handle('sendMySignal')
def send_my_signal(event: Event):
    return dp.my_signal_event_run(MySignalEvent(event))