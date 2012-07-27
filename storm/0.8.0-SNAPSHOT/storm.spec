#   The use and distribution terms for this software are covered by the Eclipse 
#   Public License 1.0 (http://opensource.org/licenses/eclipse-1.0.php) which
#   can be found in the file LICENSE.html at the root of this distribution. 
#   By using this software in any fashion, you are agreeing to be bound by 
#   the terms of this license. You must not remove this notice, or any 
#   other, from this software.

Name:          storm
Version:       0.8.0-SNAPSHOT
Release:       1%{?dist}
Summary:       Storm Complex Event Processing   
Group:         Applications/Internet
License:       EPLv1
URL:           http://storm-project.net/
Source0:        https://github.com/downloads/nathanmarz/storm/storm-%{version}.zip
Prefix:        %{_prefix}
Buildroot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, gcc-c++, libstdc++-devel
Requires:      jdk jzmq

%description
Storm integrates with any queueing system and any database system. Storm's spout 
abstraction makes it easy to integrate a new queuing system. Example queue integrations include:

1.Kestrel
2.RabbitMQ / AMQP
3.Kafka
4.JMS

Likewise, integrating Storm with database systems is easy. Simply open a connection to your database and 
read/write like you normally would. Storm will handle the parallelization, partitioning, and retrying on 
failures when necessary.

%prep
%setup -T storm-%{version}
unzip %{SOURCE0}

%build

%install
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)


