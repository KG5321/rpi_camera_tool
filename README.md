Raspberry Pi scheduled camera tool
=
Takes picture every 30 minutes. Useful when You want to create  dataset to train classifier.

## Requirements 
### Install all packages
`$ pip3 install -r requirements.txt`

### Enable Google Drive API
[Go to this page,](https://developers.google.com/drive/api/v3/quickstart/python "Google Drive API")
 enable api and download `credentials.json`

### Place `credentials.json` in project folder

## Usage

Run on Your RPi

`$ python3 rpi_camera_tool.py`

**Remember to enable camera in raspi_config before using script**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details