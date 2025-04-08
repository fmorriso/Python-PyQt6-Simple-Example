# PyQt6 Simple Example

A simple example of PyQt6

## Tools Used

| Tool      |  Version |
|:----------|---------:|
| Python    |   3.13.2 |
| PyQt6     |    6.8.1 |
| PyQt6-Qt6 |    6.9.0 |
| PyQt6-sip |  13.10.0 |
| PyCharm   | 2024.3.5 |
| VSCode    |   1.99.0 |

## Change History

| Date       | Description                        |
|:-----------|:-----------------------------------|
| 2025-04-08 | upgrade to latest software version |

## References
* []()
* 
## Developer Notes
On October 11, 2024, I ran into an error:
```text
ModuleNotFoundError  PyQt6.sip
```
The fix was to perform the following:
```text
pip install PyQt6 sip --force-reinstall
```