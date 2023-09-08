class SternmanEngine:
        def __init__(self, last_service_date: str, warning_light_is_on: bool):
                    self.last_service_date = last_service_date
                            self.warning_light_is_on = warning_light_is_on

                                def engine_should_be_serviced(self) -> bool:
                                            return self.warning_light_is_on

