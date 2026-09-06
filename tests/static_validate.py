from pathlib import Path
import re, wave, sys
root = Path(__file__).resolve().parents[1]
errors=[]

def ok(cond,msg):
    if cond: print('PASS:',msg)
    else:
        print('FAIL:',msg)
        errors.append(msg)

project = root/'project.godot'
scene = root/'scenes/piste_0/christmas_1982/Christmas1982.tscn'
ok(project.exists(),'project.godot exists')
ok(scene.exists(),'Christmas1982 main scene exists')
ptxt=project.read_text(encoding='utf-8')
ok(ptxt.count('[input]')==1,'project.godot has one input section')
ok('Christmas1982.tscn' in ptxt,'main scene points to Christmas1982')
for action in ['move_forward','move_back','move_left','move_right','interact','record','play_recording']:
    ok(re.search(rf'^{re.escape(action)}=\{{',ptxt,re.M) is not None,f'input action {action} declared')

stxt=scene.read_text(encoding='utf-8')
paths=re.findall(r'path="res://([^"]+)"',stxt)
for rel in paths:
    ok((root/rel).exists(),f'scene resource exists: {rel}')

ext_ids=set(re.findall(r'^\[ext_resource .* id="([^"]+)"\]$', stxt, re.M))
sub_ids=set(re.findall(r'^\[sub_resource .* id="([^"]+)"\]$', stxt, re.M))
for ref in re.findall(r'ExtResource\("([^"]+)"\)', stxt):
    ok(ref in ext_ids, f'ExtResource reference resolves: {ref}')
for ref in re.findall(r'SubResource\("([^"]+)"\)', stxt):
    ok(ref in sub_ids, f'SubResource reference resolves: {ref}')
load_match=re.search(r'^\[gd_scene load_steps=(\d+) format=3\]$', stxt, re.M)
if load_match:
    declared=int(load_match.group(1))
    expected=len(ext_ids)+len(sub_ids)+1
    ok(declared==expected, f'TSCN load_steps matches resources ({expected})')
else:
    ok(False, 'TSCN declares load_steps and format=3')

required_classes={
    'interaction/interactable.gd':'class_name Interactable',
    'interaction/recordable_source.gd':'class_name RecordableSource',
    'interaction/interaction_context.gd':'class_name InteractionContext',
    'recorder/recording_clip.gd':'class_name RecordingClip',
    'recorder/recorder.gd':'class_name Recorder',
    'recorder/fisher_price.gd':'class_name FisherPrice',
    'characters/malo/malo.gd':'class_name MaloController',
    'characters/common/placeholder_humanoid.gd':'class_name PlaceholderHumanoid3D',
}
for rel,needle in required_classes.items():
    txt=(root/rel).read_text(encoding='utf-8')
    ok(needle in txt,f'{needle} declared')

ctxt=(root/'interaction/interaction_context.gd').read_text(encoding='utf-8')
for needle in ['current_interactable', 'current_recordable_source', 'interact_current', 'get_current_prompt']:
    ok(needle in ctxt, f'InteractionContext implements {needle}')
ok('InteractionContext' in stxt and 'sensor_path = NodePath("../InteractionSensor")' in stxt,
   'Christmas1982 wires InteractionContext to Malo sensor')

rtxt=(root/'recorder/recorder.gd').read_text(encoding='utf-8')
for state in ['STOP','REC','PLAY']:
    ok(state in rtxt,f'Recorder contains {state} state')
for fn in ['start_recording','stop_recording','play_latest','play_clip']:
    ok(re.search(rf'^func {fn}\(',rtxt,re.M) is not None,f'Recorder implements {fn}()')
for capability in ['track_count', 'supports_pitch', 'supports_sound_on_sound']:
    ok(capability in rtxt, f'Recorder exposes future-safe capability {capability}')

cliptxt=(root/'recorder/recording_clip.gd').read_text(encoding='utf-8')
for field in ['clip_name', 'source_id', 'source_title', 'duration_seconds', 'created_unix_time', 'metadata', 'stream']:
    ok(re.search(rf'var {field}\b', cliptxt) is not None, f'RecordingClip stores {field}')

ftxt=(root/'recorder/fisher_price.gd').read_text(encoding='utf-8')
for state in ['PLACED','EQUIPPED','ACTIVE']:
    ok(state in ftxt, f'Fisher Price contains {state} device state')

mtxt=(root/'characters/malo/malo.gd').read_text(encoding='utf-8')
for fn in ['equip_recorder','try_begin_recording','try_stop_recording','try_play_latest']:
    ok(re.search(rf'^func {fn}\(',mtxt,re.M) is not None,f'Malo implements {fn}()')
ok('$InteractionContext' in mtxt,'Malo delegates proximity selection to InteractionContext')

hudtxt=(root/'ui/hud.gd').read_text(encoding='utf-8')
for ui_state in ['● REC','▶ PLAY','■ STOP']:
    ok(ui_state in hudtxt,f'HUD renders {ui_state}')

for node_name in [
    'Set', 'BackWall', 'LeftWall', 'RightWall', 'FrontBoundary',
    'RugPlaceholder', 'SofaPlaceholder', 'FireplacePlaceholder',
    'CoffeeTablePlaceholder', 'TreePlaceholder', 'GiftPile', 'Lighting',
    'FireGlow', 'TreeLamp', 'CinematicCamera'
]:
    ok(f'name="{node_name}"' in stxt, f'Christmas1982 contains visual node {node_name}')

camera=(root/'scenes/piste_0/christmas_1982/cinematic_camera.gd').read_text(encoding='utf-8')
for needle in ['_camera_anchor', '_target_anchor', 'displacement := target.global_position - _target_anchor', 'focus_height']:
    ok(needle in camera, f'cinematic camera implements {needle}')

for node_name in ['Blocking', 'MaloStart', 'FisherPickupBeat', 'RonanRecordBeat', 'RonanStand', 'CameraStart', 'VisualRig']:
    ok(f'name="{node_name}"' in stxt, f'Christmas1982 contains Sprint 3 node {node_name}')

humanoid=(root/'characters/common/placeholder_humanoid.gd').read_text(encoding='utf-8')
for needle in ['stature', 'set_motion_amount', '_build_placeholder', 'LeftArm', 'RightLeg', 'FacingMarker']:
    ok(needle in humanoid, f'PlaceholderHumanoid3D implements {needle}')
ok('visual_rig.set_motion_amount' in mtxt, 'Malo drives placeholder gait from real movement speed')

for test in ['tests/test_recorder.gd','tests/test_gameplay_contract.gd','tests/test_visual_contract.gd','tests/test_blocking_contract.gd']:
    ok((root/test).exists(), f'{test} exists')

wav=root/'audio/ronan_test.wav'
try:
    with wave.open(str(wav),'rb') as w:
        duration=w.getnframes()/w.getframerate()
        ok(w.getnchannels()==1,'RonanTest placeholder audio is mono')
        ok(duration>=4.9,'RonanTest placeholder audio is ~5 seconds')
except Exception as e:
    errors.append(f'WAV invalid: {e}')
    print('FAIL: WAV invalid',e)

print(f'\nStatic validation complete: {len(errors)} failure(s).')
sys.exit(1 if errors else 0)
