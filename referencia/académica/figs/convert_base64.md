1. base64 -w 0 copilot-edits-view-edits-in-file.png > copilot-edits-view-edits-in-file.b6
2. Append at the start of the only line `![image.png](data:image/png;base64,`
    - Vim `gg`, then insert a line.
3. Append at end of that line `)` to close the parenthesis.
    - Vim `$`, then insert `)`.
