# coding=utf-8
import power


class TestObserver(power.PowerManagementObserver):
    def on_power_sources_change(self, power_management):
        print("on_power_sources_change")

    def on_time_remaining_change(self, power_management):
        print("on_time_remaining_change")


if __name__ == "__main__":
    o = TestObserver()
    p = power.PowerManagement()
    p.add_observer(o)
    try:
        print("Power management observer is registered")
        import time
        while True:
            time.sleep(1)
    finally:
        p.remove_observer(o)
