# Smart Protein Dispensing System

## Overview

This assignment analyzes a common physical object, the protein powder container and scoop system, and proposes a redesigned version that integrates sensing and intelligent feedback to improve usability, reliability, and everyday workflow fit.

Rather than treating the container as a passive storage vessel, this project reframes it as a high-frequency interaction object that plays a role in daily routines. By examining where the current design fails to meet real-world usage patterns, this redesign aims to reduce friction, improve feedback, and better integrate into everyday life.


## Everyday Object Selected

Protein powder container with scoop

This object is not just a container, but it also defines a workflow:

Go to Cabinet → Open → Scoop → Level → Pour → Close → Return to Cabinet

This workflow occurs frequently, often under time pressure and fatigue, making it an ideal choice to examine for usability analysis.

## Object Analysis & Missing Affordances
#### Awareness Gaps

• Gap 1: No awareness of serving size accuracy (system doesn't know reality)

Use scenario: A user wants consistent protein intake but relies on eyeballing scoop size.  
The gap: The system cannot detect or control how much is actually dispensed.  
Opportunity: The object could dispense precise amounts or detect inconsistencies.  
Justification: Scoop-based measurement is unreliable. This is a real accuracy problem, not a novelty feature.  

#### Feedback Gaps
• Gap 2: No confirmation of successful action (user doesn't know reality)

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

Old product and workflow:
Go to Cabinet → Open → Scoop → Level → Pour → Close → Return to Cabinet

New product and workflow:
Place cup → Press button → Receive exact amount


### Design Rationale
This redesign prioritizes moment-of-use friction rather than long-term habit optimization. While the object presents opportunities for anticipation (e.g., learning routines), the core usability failure occurs during the physical act of dispensing: the current system requires fine motor control, visual attention, and repeated manual steps to accomplish a simple, habitual task.

The redesign specifically addresses the following gaps:

• Awareness Gap (Gap 1): By integrating a load cell, the system gains awareness of the quantity being dispensed, enabling consistent dosing.

• Feedback Gap (Gap 2): Visual and audio confirmation replace guesswork, reducing cognitive uncertainty.

• Adaptation Gap (Gap 3): User-set portion preferences allow the system to accommodate different nutritional goals.

• Contextual Fit Gap (Gap 4): The single-action dispense mechanism supports one-handed, low-attention interaction.

• Social Fit Gaps (Gaps 6–7): The form factor is designed to integrate into kitchen environments without performative or explanatory cost, and the workflow is compressed into a single step.

Gap 5 was intentionally not addressed. While predictive features could be added, they would increase system complexity without meaningfully improving the core interaction problem. The primary friction is not remembering to make a shake, but the physical and cognitive effort required to prepare one repeatedly. This redesign therefore focuses on improving reliability and ease at the moment of use rather than automating scheduling.

### Proposed Features

• Sensors

    • Load cell (weight sensor): Tracks remaining quantity and ensures accurate dosing

    • Proximity or capacitive sensor: Detects when a cup is present

• Actuators

    • Motorized auger: Dispenses controlled amounts

• LCD Display: Shows weight

• Audio feedback: Confirms successful dispense (maybe)

Proposed feature justification: This redesign requires sensing and computational logic because precision, feedback, and adaptation cannot be reliably achieved through passive mechanical design alone. Load-based measurement enables dynamic adjustment for different powders with varying densities, which volumetric scoops cannot accommodate. Feedback systems allow the object to surface hidden internal states (remaining quantity, dosing accuracy), which traditional containers cannot communicate.

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

This redesign introduces additional components (sensors, a motor, and basic control logic) that increase complexity compared to a passive container. However, these tradeoffs are intentionally low-risk.

If any component fails, the system degrades gracefully rather than complete failure. The user can always open the lid and revert to manual scooping, preserving the original functionality. This ensures that no failure mode prevents access to the product itself.

Added Complexity

The inclusion of a motorized dispensing mechanism introduces the possibility of mechanical jamming or wear. However, because the object is not safety-critical, these failures result in inconvenience rather than harm.

Calibration and Accuracy

Weight-based sensing may require occasional recalibration. While this adds minor maintenance overhead, it enables more reliable dosing than volumetric scoops, which are inherently inconsistent.

Power Dependence

The system requires wall power, introducing a dependency that does not exist in traditional containers. However, loss of power does not block access to the powder, it only disables the automated convenience.

Cost

This design would be more expensive than disposable tubs, shifting the object from packaging to a semi-durable appliance. This tradeoff is justified by its repeated daily use and long-term convenience.

Why This Tradeoff Is Acceptable

This object is designed to fail softly. No single failure prevents the core task from being completed. Instead, the system offers convenience when functioning and reverts to familiar interaction when not.

This makes the added improvements appropriate: it improves usability without introducing fragile dependency.
