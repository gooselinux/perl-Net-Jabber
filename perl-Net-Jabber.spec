# $Id$

Name:           perl-Net-Jabber
Version:        2.0 
Release:        12%{?dist}
Summary:        Net::Jabber - Jabber Perl Library

Group:          Development/Libraries
License:        (GPL+ or Artistic) or LGPLv2+
URL:            http://search.cpan.org/dist/Net-Jabber/
Source0: http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/Net-Jabber-%{version}.tar.gz 
Source1:        LICENSING.correspondance
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl, perl(Net::XMPP), perl(Time::Timezone)
BuildRequires:  perl(ExtUtils::MakeMaker)

Requires:  perl(Time::Timezone)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Net::Jabber provides a Perl user with access to the Jabber Instant
Messaging protocol.

For more information about Jabber visit:

    http://www.jabber.org

%prep
%setup -q -n Net-Jabber-%{version}

cp %{SOURCE1} .

# generate our other two licenses...
perldoc perlgpl > LICENSE.GPL
perldoc perlartistic > LICENSE.Artistic

# we really don't want executable examples...
chmod -x examples/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

# fix wonky execute permissions
find %{buildroot} -type f -exec chmod -x '{}' ';'

%check
# Disable tests which will fail under mock
rm t/protocol_definenamespace.t
rm t/protocol_muc.t
rm t/protocol_rpc.t

make test


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES README examples LICENSE.* LICENSING.*
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.0-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0-9
- fix license tag (technically, it was correct before, but this change prevents
  rpmlint from flagging it as bad in a false positive)

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0-8
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.0-7.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.0-7
- bump for mass rebuild

* Mon Jul 10 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.0-6
- release bump to make fc5->fc6 reports happy :)

* Tue May 30 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.0-5
- disable tests which will fail under mock
- remove execute bits from files which shouldn't have them
- include additional buildreq of perl(Time::Timezone)
- also include perl(Time::Timezone) as a requires, as it provides optional
  functionality and is not picked up by the autoreq/prov scripts.

* Thu May 25 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.0-4
- include license text, including generated ones
- include correspondance with the module's author

* Wed May 24 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.0-3
- update license to triple licensed, based on conversations with upstream

* Mon May 15 2006 Chris Weyl 2.0-2
- add additional files as docs

* Fri May 12 2006 Chris Weyl 2.0-1
- first f-e spec

