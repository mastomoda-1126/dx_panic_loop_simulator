import random
import time

class LegacyDXBackend:
    """
    Satirical DX backend:
    - No stable infra
    - No proper data model
    - Loves to blame 'user side'
    """

    def __init__(self):
        self.state = "confused"

    def process_request(self, payload: dict) -> str:
        event = random.choice(
            ["network_down", "schema_missing", "unclear_requirement", "just_panic"]
        )
        print(f"\n[DX] Incoming request: {payload}")
        print(f"[DX] Internal event: {event}")

        if event == "network_down":
            return self._fallback("Network is unstable.")
        elif event == "schema_missing":
            return self._fallback("We never designed the data model.")
        elif event == "unclear_requirement":
            return self._fallback("Requirements are unclear, let's form a committee.")
        else:  # just_panic
            return self._fallback("We are still 'discussing' the DX vision.")

    def _fallback(self, reason: str) -> str:
        print(f"[DX] Panic mode ON. Reason: {reason}")
        print("[DX] We will support everybody by... printing documents.")
        return "PRINT_HANDOUTS"


class FrontlineClient:
    """
    Represents frontline staff reacting to DX chaos.
    """

    def __init__(self, name: str):
        self.name = name

    def handle_response(self, response: str):
        print(f"\n[Frontline:{self.name}] Got response from DX: {response}")
        if response == "PRINT_HANDOUTS":
            self._panic_and_print()
        else:
            print(f"[Frontline:{self.name}] Somehow it worked today…?")

    def _panic_and_print(self):
        printer_issue = random.choice(["paper_jam", "no_toner", "works_fine_but_late"])
        print(f"[Frontline:{self.name}] Switching to paper mode…")

        if printer_issue == "paper_jam":
            print(f"[Frontline:{self.name}] Printer jammed. Panic continues.")
        elif printer_issue == "no_toner":
            print(f"[Frontline:{self.name}] No toner. Running around the building.")
        else:
            print(f"[Frontline:{self.name}] Printed everything, but lost half of the time slot.")


class PanicLoopSimulation:
    """
    Connects LegacyDXBackend and FrontlineClient
    to show the full panic-driven loop.
    """

    def __init__(self, iterations: int = 5):
        self.iterations = iterations
        self.backend = LegacyDXBackend()
        self.frontline = FrontlineClient(name="Unit A")

    def run(self):
        """Finite demo run (safe)."""
        print("=== Panic-Driven DX Simulation Start ===")
        for i in range(1, self.iterations + 1):
            print(f"\n--- Cycle {i} ---")
            payload = {
                "unit": "A-1",
                "content": "operational_materials",
                "desired_format": "digital"
            }
            response = self.backend.process_request(payload)
            self.frontline.handle_response(response)
            time.sleep(0.2)
        print("\n=== Simulation End ===")

    def run_infinite(self):
        """
        Infinite panic loop version.

        WARNING:
            This is intentionally an infinite loop to model
            organizations that never exit panic mode.
            DO NOT CALL THIS in real environments unless you
            are okay with the process hanging forever.
        """
        print("=== Panic-Driven DX Infinite Loop (DO NOT RUN IN REAL LIFE) ===")
        cycle = 0
        while True:
            cycle += 1
            print(f"\n--- Infinite Cycle {cycle} ---")
            payload = {
                "unit": "A-1",
                "content": "operational_materials",
                "desired_format": "digital"
            }
            response = self.backend.process_request(payload)
            self.frontline.handle_response(response)
            time.sleep(0.2)


if __name__ == "__main__":
    sim = PanicLoopSimulation(iterations=5)
    sim.run()

    # NOTE:
    #   The "true" panic-driven DX never ends.
    #   The method below intentionally creates an infinite loop.
    #   It is commented out to avoid crashing / hanging your environment.
    #
    #   Uncomment at your own risk if you really want to see
    #   what endless panic looks like in your terminal.
    #
    # sim.run_infinite()
