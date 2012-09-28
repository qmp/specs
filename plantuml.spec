#TODO : maven based build
#SEE : https://fedoraproject.org/wiki/Packaging:Java?rd=Packaging/Java#Introduction
#based on http://yar.fruct.org/projects/plantuml-deb
#also based on http://aur.archlinux.org/packages/pl/plantuml/PKGBUILD
Name:           plantuml
Version:        7935
Release:        2%{?dist}
Summary:        Program to generate UML diagram from a text description 

License:        GPLv3+
URL:            http://plantuml.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.runscript


BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  ant
Requires:       java
Requires:       jpackage-utils
Requires:       graphviz

BuildArch:      noarch

%description
PlantUML is a program allowing to draw UML diagrams, using a simple and human
readable text description. It is extremely useful for code documenting,
sketching project architecture during team conversations and so on.

PlantUML supports the following diagram types:
 - sequence diagram
 - use case diagram
 - class diagram
 - activity diagram
 - component diagram
 - state diagram

#%package  javadoc
#Summary:        API documentation for %{name}

#%description javadoc
#%{summary}

%prep
%setup -q


%build
ant dist


%install
install -d -m 755 %{buildroot}/%{_javadir}
install -p -m 644 %{name}.jar %{buildroot}/%{_javadir}/%{name}.jar
install -d -m 755 %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}


%files
%doc
%{_bindir}/%{name}
%{_javadir}/%{name}.jar

#%files javadoc
#%{_javadocdir}/%{name}



%changelog
* Fri Sep 28 2012 qmp <glang@lavabit.com> 7935-2
 - Fix path in run script

* Fri Sep 28 2012 qmp <glang@lavabit.com> 7935-1
 - Initial packaging
