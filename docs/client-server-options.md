# Client-Server Options and Commands

## Overview

This document outlines the key commands and configurations for managing the client-server setup in FreeCiv, including console commands and game options.

## Console Commands

### Key Commands

- `/show`: Displays all changeable options
- `/help`: Lists available tools and commands
- `/set`: Modifies in-game options

### Game Configuration Commands

#### Player Management

```plaintext
/set minplayers __
# Example: Set minimum players to 2
/set minplayers 2
```

#### Turn Management

```plaintext
/set timeout __
# Example: Set turn timeout to 60 seconds
/set timeout 60
```

#### Game Duration

```plaintext
/set endt __
# Example: Set maximum turns to 500
/set endt 500
```

## Client-Server Setup

### Headless Mode

To run the server without a client:

1. Set `minplayers` to 0
2. Change all players to AI using `aitoggleplayer`
3. Set `timeout` to 1 second
4. Disable map features in game options
5. Optionally set `endt` for max turns

**Example Configuration:**

```plaintext
/set minplayers 0
/set timeout 1
```

### Server-Only Operation

Running without a client allows for:

- Automated gameplay
- Reduced resource usage
- Scripted game control

**Note:** Final scores may be difficult to obtain without a client.

## Use Cases

1. **Automated Testing:** Run games without user intervention
2. **Performance Analysis:** Measure AI performance under different configurations
3. **Scripted Scenarios:** Use console commands to control game flow programmatically
