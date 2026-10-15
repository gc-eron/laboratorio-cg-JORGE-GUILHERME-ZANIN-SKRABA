let
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixos-26.05.tar.gz") {};
in

pkgs.mkShell {
  packages = [
    (pkgs.python312.withPackages (python-pkgs: with python-pkgs; [
      # select Python packages here
      streamlit
      numpy
      opencv4
      matplotlib
      pillow
    ]))
  ];
}