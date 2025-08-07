package accesscontrol

default out := {
  "allow": false,
  "step_up_auth": false,
  "deny": false
}

out := {
  "allow": true,
  "step_up_auth": false,
  "deny": false
} if input.risk < 0.5

out := {
  "allow": false,
  "step_up_auth": true,
  "deny": false
} if input.risk >= 0.5 {
  input.risk < 0.75
}

out := {
  "allow": false,
  "step_up_auth": false,
  "deny": true
} if input.risk >= 0.75