Summary:	Application for converting different XML schema languages to and from RELAX NG
Summary(pl.UTF-8):	Aplikacja do konwersji różnych języków schematów XML na i z RELAX NG
Name:		trang
Version:	20091111
Release:	1
License:	BSD
Group:		Applications/Text
#Source0Download: http://code.google.com/p/jing-trang/downloads/list
Source0:	http://jing-trang.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	9d31799b948c350850eb9dd14e5b832d
URL:		http://code.google.com/p/jing-trang/
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trang is an application for converting different XML schema languages
to and from RELAX NG.

%description -l pl.UTF-8
Trang to aplikacja do konwersji różnych języków schematów XML na i z
RELAX NG.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}

install trang.jar $RPM_BUILD_ROOT%{_javadir}

cat >$RPM_BUILD_ROOT%{_bindir}/trang <<'EOF'
#!/bin/sh

java -jar %{_javadir}/trang.jar "$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc copying.txt trang-manual.html
%attr(755,root,root) %{_bindir}/trang
%{_javadir}/trang.jar
