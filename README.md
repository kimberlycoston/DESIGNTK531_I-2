# Smart Protein Dispensing System

## Overview

This assignment analyzes a common physical object—the protein powder container and scoop system—and proposes a redesigned version that integrates sensing and intelligent feedback to improve usability, reliability, and everyday workflow fit.

Rather than treating the container as a passive storage vessel, this project reframes it as a high-frequency interaction object that plays a role in daily routines. By examining where the current design fails to meet real-world usage patterns, this redesign aims to reduce friction, improve feedback, and better integrate into everyday life.


## Everyday Object Selected

Protein powder container with scoop

This object is not just a container, but it also defines a workflow:

Go to Cabinet → Open → Scoop → Level → Pour → Close → Return to Cabinet

This workflow occurs frequently, often under time pressure and fatigue, making it an ideal choice to examine for usability analysis.

## Object Analysis & Missing Affordances
#### Awareness Gaps

• Gap 1: No awareness of serving size accuracy

Use scenario: A user wants consistent protein intake but relies on eyeballing scoop size.  
The gap: The system cannot detect or control how much is actually dispensed.  
Opportunity: The object could dispense precise amounts or detect inconsistencies.  
Justification: Scoop-based measurement is unreliable. This is a real accuracy problem, not a novelty feature.  

#### Feedback Gaps
• Gap 2: No confirmation of successful action

Use scenario: Similar to above. A user wants consistent protein intake but relies on eyeballing scoop size.  
The gap: There is no feedback confirming that the correct amount was dispensed.  
Opportunity: The system could provide visual, haptic, or auditory confirmation.  
Justification: Feedback is a foundational usability principle. The current system assumes perfect human action.  


#### Adaptation Gaps
• Gap 3: One-size-fits-all interaction

Use scenario: Different users want different amounts.  
The gap: The container treats all users and contexts the same.  
Opportunity: The system could adapt to user preferences.  
Justification: The object currently ignores variation in user needs.  

• Gap 4: No accommodation for constrained contexts

Use scenario: The user is holding a shaker, phone, or coffee and is rushed.  
The gap: The system requires two hands, visual attention, and fine motor control.  
Opportunity: It could support one-handed or low-attention interaction.  
Justification: This is a real mismatch between designed and actual usage.  

#### Anticipation Gaps
• Gap 5: No learning of routines

Use scenario: The user makes a shake at roughly the same time each day.  
The gap: The object treats every interaction as new.  
Opportunity: It could learn patterns and prepare or prompt accordingly (like the automatic coffee pots)  
Justification: Many everyday objects already adapt to routine behavior to reduce habitual friction.  

#### Social Fit Gaps
• Gap 6: Visual and spatial clutter

Use scenario: Large protein tubs are stored awkwardly or left on counters, decreasing overall kitchen aesthetic.  
The gap: The design prioritizes shipping and branding over domestic integration.  
Opportunity: A redesign could be compact, discreet, and space-efficient.  
Justification: Objects must fit socially and spatially into real homes.  

• Gap 7: Cumbersome daily ritual

Use scenario: Daily repeated use.  
The gap: The system requires a multi-step interaction for a simple task.  
Opportunity: The interaction could be compressed into a single action.  
Justification: Repetitive tasks should become easier, not remain equally demanding.  

## 2. Proposed Redesign

The redesign replaces the scoop-based workflow with a single-step dispensing interaction.  

Instead of:
Go to Cabinet → Open → Scoop → Level → Pour → Close → Return to Cabinet

The new flow becomes:
Place cup → Press button → Receive exact amount

* The primary friction in this workflow is not remembering when to make a shake, but the physical and cognitive effort required during the act of dispensing. Automating timing would add system complexity without meaningfully improving the core usability problem. For this reason, the redesign prioritizes improving moment-of-use interaction rather than predictive scheduling, thus, I chose not to address gap 5 listed above.

### Design Rationale
ENTER STUFF HERE

### Proposed Features

• Sensors

• Load cell (weight sensor): Tracks remaining quantity and ensures accurate dosing

• Proximity or capacitive sensor: Detects when a cup is present

• Actuators

• Motorized auger: Dispenses controlled amounts

• LED: Shows status and warnings

• Audio feedback: Confirms successful dispense


### Social Considerations
• Habit Replacement

The redesign replaces scooping but preserves the core routine: making a shake.

• Visibility

The system is designed to be quiet, compact, and non-performative.

• Social Cost

Low. It resembles familiar kitchen appliances and does not require explanation.

• Behavior Change

Minimal. The only new action is pressing a button instead of scooping.

### Tradeoff Analysis  

• New Costs

• Sensors and motors

• Manufacturing complexity

• Maintenance

New Failure Modes
Failure	Risk    |   Mitigation
Motor jam   |   No dispense |   Manual override
Sensor drift    |	Inaccuracy  |   Periodic calibration
Power loss  |   Unusable    |   Removable Lid

Why This Tradeoff Is Worth It:

This redesign addresses cumulative habitual friction. Small inefficiencies become meaningful when repeated daily. The goal is reliability, reduced effort, and better workflow fit.
