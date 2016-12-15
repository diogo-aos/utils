import i3


def move_workspace(workspace, output):
    i3.command('workspace', workspace['name'])
    i3.command('move', 'workspace to output ' + output['name'])
    i3.command('workspace', workspace['name'])

outputs = i3.get_outputs()
workspaces = i3.get_workspaces()

f_ws = [ws for ws in workspaces if ws['focused']][0]  # focused workspace
f_output = [o for o in outputs if o['name'] == f_ws['output']][0]  # focused output
a_outputs = [o for o in outputs if o['active']]  # active outputs

# if there is only 1 output available, nothing to do
if len(a_outputs) != 1:
    idx = a_outputs.index(f_output)
    next_output = a_outputs[(idx + 1) % len(a_outputs)]
    for ws in workspaces:
        move_workspace(ws, next_output)
