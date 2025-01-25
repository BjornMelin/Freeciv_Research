# AI Behavior Traits in Freeciv

## Overview

Freeciv AI behavior is governed by three core traits that influence strategic decision-making:

- **Expansionist**: Drives territory expansion and city founding
- **Trader**: Controls trade route establishment and economic focus
- **Aggression**: Determines likelihood of declaring war

Default trait values are set to 50 for all nations, but can be modified through ruleset edits or Lua scripting.

## Trait Configuration

### 1. Ruleset Modification

Edit nation files in `Freeciv-2.5.11\data\civ2\nation`:

```ini
# Example: Make Romans more expansionist
trait_expansionist = 75
```

### 2. Lua Scripting

Use the `edit.trait_mod` function during gameplay:

```lua
-- Increase aggression for player 3 by 20 points
edit.trait_mod(3, "aggression", 20)
```

## Trait Details

### Expansionist

**Behavioral Impact:**

- Prioritizes settler production
- Favors frontier city locations
- Invests in exploration

**Recommended Adjustments:**

- ↑ For wide empire strategies
- ↓ For tall civilization playstyles

### Trader

**Behavioral Impact:**

- Focuses on marketplace construction
- Prioritizes trade route establishment
- Values luxury resources

**Recommended Adjustments:**

- ↑ For economic victory conditions
- ↓ For militaristic civilizations

### Aggression

**Behavioral Impact:**

- Increases military unit production
- Lowers diplomatic relationship thresholds
- Favors offensive technologies

**Recommended Adjustments:**

- ↑ For domination-focused AIs
- ↓ For peaceful cultural strategies

## File References

Trait logic is implemented in:

- `\ai\aicity` (City management)
- `\ai\advdiplomacy` (Diplomatic decisions)
- `\ai\advdomestic` (Economic planning)

## AI Development Use Cases

1. **Scenario Design:** Create custom AI personalities by combining trait values
2. **Balance Testing:** Compare different trait configurations
3. **Adaptive AI:** Implement dynamic trait adjustments based on game state
