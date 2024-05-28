<a name="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<br />
<div align="center">
  <a href="https://github.com/obeidahmad/family-media-sorter">
    <img src="images/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Media Sorter</h3>

  <p align="center">
    A simple script to sort your media!
    <br />
    <a href="https://github.com/obeidahmad/family-media-sorter"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/obeidahmad/family-media-sorter">View Demo</a>

[//]: # (    ·)

[//]: # (    <a href="https://github.com/obeidahmad/family-media-sorter/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>)

[//]: # (    ·)

[//]: # (    <a href="https://github.com/obeidahmad/family-media-sorter/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>)
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li>
            <a href="#usage">Usage</a>
            <ul>
                <li><a href="#create-of-the-exec-file">Creation of the Exec File</a></li>
                <li><a href="#executing-the-exec-file">Executing the Exec File</a></li>
                <li><a href="#extra-options">Extra Options</a></li>
            </ul>
        </li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



## About The Project

There are many great media sorters out there, but none really suited me. So I created my own. The main idea here is simplicity, and the ability to sort even media who has missing or unusual tags.
This app is built with [![Python][Python]][Python-url] and leverages [![ExifTool][ExifTool]][ExifTool-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Getting Started

### Prerequisites

- You first need to have ExifTool (minimum version of 12.15) installed from [here][ExifTool-url].
Make sure to follow the steps in the [official docs][ExifTool-tutorial-url].
- Download the latest stable solution from [here][project-latest-release].

> **_NOTE:_**  Currently only Linux is supported.

### Usage

Now everything is installed, you should know that the solution is made of 2 independent but complimentary steps:

#### Creation of the Exec File

To generate the exec file:
```sh
app -m create <media_dir> <new_dir>
```
A file of the name `exec_file.json` will be created.

The `Exec File` is a json file that contains the different media files found. In that file they will be mapped to there new desired location
in addition to some parameters.
Typically, it would look like the following:
```json
{
  "$options": {
    "mode": "COPY",
    "delete_empty_dir": true,
    "delete_error_files": true,
    "delete_exec_file": true
  },
  "path_mapping": {
    "new_dir":{
      "YYYY.MM": {
        "Camera": {
          "date.png": "old_path"
        }
      },
      ...
    },
    ...
  },
  "errors": {
    "error_file_path": "error_message",
    ...
  }
}
```

As you can see `$option` contains the different settings,
`path_mapping` contains the mapping starting with a tree structure for the new path mapped to the old path,
`errors` contains all the paths of the unrecognized files (or any other error that would show as the _error_message_) 

The new path created is in the following format `new_dir/YYYY.MM/Camera/date.png`.
You can change anything in this file as long as you keep the structure. Thus, allowing you to have complete control. 

#### Executing the Exec File

After creating the Exec File you can execute it using:
```sh
app -m execute
```

#### Extra Options

If you need to see all available options use:
```sh
app -h
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Roadmap

- [x] Add Linux Support
- [ ] Add Windows Support
- [ ] Allow for more control during the creation of the Exec File
- [ ] Create version with packaged ExifTool
- [ ] Use a better file structure than Json 

See the [open issues](https://github.com/obeidahmad/family-media-sorter/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contributing

Any contribution is **greatly appreciated**.
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

You can also fork the project and submit a pull request.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## License

Distributed under the Apache-2.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contact

Ahmad Obeid - obeid.ahmad2001@outlook.com

Project Link: [https://github.com/obeidahmad/family-media-sorter](https://github.com/obeidahmad/family-media-sorter)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Acknowledgments

The amazing resources and library that made this project possible:

* [ExifTool](https://github.com/exiftool/exiftool)
* [PyExifTool](https://github.com/sylikc/pyexiftool)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/obeidahmad/family-media-sorter.svg?style=for-the-badge
[contributors-url]: https://github.com/obeidahmad/family-media-sorter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/obeidahmad/family-media-sorter.svg?style=for-the-badge
[forks-url]: https://github.com/obeidahmad/family-media-sorter/network/members
[stars-shield]: https://img.shields.io/github/stars/obeidahmad/family-media-sorter.svg?style=for-the-badge
[stars-url]: https://github.com/obeidahmad/family-media-sorter/stargazers
[issues-shield]: https://img.shields.io/github/issues/obeidahmad/family-media-sorter.svg?style=for-the-badge
[issues-url]: https://github.com/obeidahmad/family-media-sorter/issues
[license-shield]: https://img.shields.io/github/license/obeidahmad/family-media-sorter.svg?style=for-the-badge
[license-url]: https://github.com/obeidahmad/family-media-sorter/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ahmad-obeid-487a8a204/
[Python]: https://img.shields.io/badge/python3.10-3776AB?logo=python&logoColor=white
[Python-url]: https://www.python.org/
[ExifTool]: https://img.shields.io/badge/exiftool-red.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8c3ZnIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiIHZpZXdCb3g9IjM1LjE5OTk5OTk5OTk5OTk5NiAzMCAxMzUuMjAwMDAwMDAwMDAwMDIgMTQwLjc5OTk5OTk5OTk5OTk4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMCIgc3R5bGU9Im1heC1oZWlnaHQ6IDUwMHB4IiB3aWR0aD0iMTM1LjIwMDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjE0MC43OTk5OTk5OTk5OTk5OCI+Cgo8ZyBzdHJva2U9Im5vbmUiIGZpbGw9IiMwMDAwMDAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuMDAwMDAwLDIwMC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiPgo8cGF0aCBkPSJNMzcwIDExMDUgbDAgLTU2NSAzMzAgMCAzMzAgMCAwIDcwIDAgNzAgLTI1NSAwIC0yNTUgMCAwIDE5MCAwIDE5MCYjMTA7MjU1IDAgMjU1IDAgMCA2NSAwIDY1IC0yNTUgMCAtMjU1IDAgMCAxNzUgMCAxNzUgMjU1IDAgMjU1IDAgMCA2NSAwIDY1IC0zMzAmIzEwOzAgLTMzMCAwIDAgLTU2NXoiLz4KPHBhdGggZD0iTTc2MCAxMzcwIGwwIC03MCAxOTAgMCAxOTAgMCAwIC00OTUgMCAtNDk1IDgwIDAgODAgMCAwIDQ5NSAwIDQ5NSYjMTA7MTkwIDAgMTkwIDAgMCA3MCAwIDcwIC00NjAgMCAtNDYwIDAgMCAtNzB6Ii8+CjwvZz4KPC9zdmc+Cg==
[ExifTool-url]: https://www.exiftool.org/
[ExifTool-tutorial-url]: https://exiftool.org/install.html
[project-latest-release]: https://github.com/obeidahmad/family-media-sorter/releases/latest