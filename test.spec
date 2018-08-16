Name: test
Version: 0.1.0
Release:        1%{?dist}
Summary: This is a test spec

License: MIT
Source0: foo.go

BuildRequires: go-toolset-1.10

%description

Test package.


%prep
%autosetup

%build

%gobuild foo.go

%configure


%check

./foo

%files
%license
%doc Test

