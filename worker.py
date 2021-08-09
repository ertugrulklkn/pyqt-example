import sys
import traceback

from PySide2.QtCore import QObject, QRunnable, Signal, Slot


class WorkerSignals(QObject):
    error = Signal(tuple)
    result = Signal(object)
    finished = Signal()
    serialEventCallback = Signal(str)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs) -> None:
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['serialEventCallback'] = self.signals.serialEventCallback

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.emit(exctype, value, traceback.format_exc())
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
