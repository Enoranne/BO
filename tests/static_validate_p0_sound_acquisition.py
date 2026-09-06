from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
errors = []


def ok(condition: bool, message: str) -> None:
    if condition:
        print("PASS:", message)
    else:
        print("FAIL:", message)
        errors.append(message)

queue_path = root / "data/p0_sound_acquisition_queue.json"
matrix_path = root / "data/p0_sound_production_matrix.json"

ok(queue_path.exists(), "P0 sound acquisition queue exists")
ok(matrix_path.exists(), "P0 sound production matrix exists")

if queue_path.exists() and matrix_path.exists():
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    family_ids = {f["id"] for f in matrix.get("families", [])}
    batches = queue.get("batches", [])

    ok(queue.get("status") == "planning_only", "acquisition queue remains planning-only")
    ok([b.get("id") for b in batches] == ["A_existing_salon", "B_microhub_expansion", "C_wider_world"], "acquisition batches remain ordered A -> B -> C")

    seen = []
    for batch in batches:
        items = batch.get("items", [])
        orders = [item.get("order") for item in items]
        ok(orders == list(range(1, len(items) + 1)), f"{batch.get('id')}: item order is contiguous")
        for item in items:
            family = item.get("family")
            seen.append(family)
            ok(family in family_ids, f"{batch.get('id')}: {family} exists in production matrix")
            if item.get("generation_fallback_allowed"):
                ok(item.get("credits_preapproval_required") is True, f"{family}: generated fallback requires credit preapproval")

    ok(seen[:4] == ["fisher_button_mechanics", "fisher_transport_click", "ronan_test", "fireplace_crackle"], "Batch A prioritises recorder feel before world expansion")
    ok("street_moped_pass" in seen and batches[-1]["items"][0]["family"] == "street_moped_pass", "moped remains deferred to wider-world Batch C")

print(f"\nP0 sound acquisition validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
