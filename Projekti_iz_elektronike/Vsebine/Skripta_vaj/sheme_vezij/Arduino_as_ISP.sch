<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="yes" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="24" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="no" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="no" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="no" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="no" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="no" active="yes"/>
<layer number="99" name="SpiceOrder" color="7" fill="1" visible="no" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="Arduino_DWD">
<packages>
<package name="ARDUINO_NANO">
<description>&lt;b&gt;Arduino Nano V3.0&lt;/b&gt;&lt;br&gt;
&lt;p&gt;The Nano was designed and is being produced by Gravitech.&lt;br&gt;

&lt;a href="http://www.gravitech.us/arna30wiatp.html"&gt;Gravitech Arduino Nano V3.0&lt;/a&gt;&lt;/p&gt;</description>
<hole x="-22.86" y="-7.62" drill="1.778"/>
<pad name="1" x="-20.32" y="-7.62" drill="0.8" shape="square"/>
<pad name="2" x="-17.78" y="-7.62" drill="0.8"/>
<pad name="3" x="-15.24" y="-7.62" drill="0.8"/>
<pad name="4" x="-12.7" y="-7.62" drill="0.8"/>
<pad name="5" x="-10.16" y="-7.62" drill="0.8"/>
<pad name="6" x="-7.62" y="-7.62" drill="0.8"/>
<pad name="7" x="-5.08" y="-7.62" drill="0.8"/>
<pad name="8" x="-2.54" y="-7.62" drill="0.8"/>
<pad name="9" x="0" y="-7.62" drill="0.8"/>
<pad name="10" x="2.54" y="-7.62" drill="0.8"/>
<pad name="11" x="5.08" y="-7.62" drill="0.8"/>
<pad name="12" x="7.62" y="-7.62" drill="0.8"/>
<pad name="13" x="10.16" y="-7.62" drill="0.8"/>
<pad name="14" x="12.7" y="-7.62" drill="0.8"/>
<pad name="15" x="15.24" y="-7.62" drill="0.8"/>
<pad name="16" x="15.24" y="7.62" drill="0.8"/>
<pad name="17" x="12.7" y="7.62" drill="0.8"/>
<pad name="18" x="10.16" y="7.62" drill="0.8"/>
<pad name="19" x="7.62" y="7.62" drill="0.8"/>
<pad name="20" x="5.08" y="7.62" drill="0.8"/>
<pad name="21" x="2.54" y="7.62" drill="0.8"/>
<pad name="22" x="0" y="7.62" drill="0.8"/>
<pad name="23" x="-2.54" y="7.62" drill="0.8"/>
<pad name="24" x="-5.08" y="7.62" drill="0.8"/>
<pad name="25" x="-7.62" y="7.62" drill="0.8"/>
<pad name="26" x="-10.16" y="7.62" drill="0.8"/>
<pad name="27" x="-12.7" y="7.62" drill="0.8"/>
<pad name="28" x="-15.24" y="7.62" drill="0.8"/>
<pad name="29" x="-17.78" y="7.62" drill="0.8"/>
<pad name="30" x="-20.32" y="7.62" drill="0.8"/>
<hole x="-22.86" y="7.62" drill="1.778"/>
<hole x="17.78" y="7.62" drill="1.778"/>
<hole x="17.78" y="-7.62" drill="1.778"/>
<wire x1="-24.13" y1="8.89" x2="19.05" y2="8.89" width="0.127" layer="21"/>
<wire x1="19.05" y1="8.89" x2="19.05" y2="3.81" width="0.127" layer="21"/>
<wire x1="19.05" y1="3.81" x2="19.05" y2="-3.81" width="0.127" layer="21"/>
<wire x1="19.05" y1="-3.81" x2="19.05" y2="-8.89" width="0.127" layer="21"/>
<wire x1="19.05" y1="-8.89" x2="-24.13" y2="-8.89" width="0.127" layer="21"/>
<wire x1="-24.13" y1="-8.89" x2="-24.13" y2="2.54" width="0.127" layer="21"/>
<wire x1="-24.13" y1="2.54" x2="-24.13" y2="8.89" width="0.127" layer="21"/>
<wire x1="-24.13" y1="2.54" x2="-25.4" y2="2.54" width="0.127" layer="21"/>
<wire x1="-25.4" y1="2.54" x2="-25.4" y2="-2.54" width="0.127" layer="21"/>
<wire x1="-19.05" y1="-2.54" x2="-19.05" y2="2.54" width="0.127" layer="21"/>
<wire x1="-19.05" y1="2.54" x2="-24.13" y2="2.54" width="0.127" layer="21"/>
<wire x1="-19.05" y1="-2.54" x2="-25.4" y2="-2.54" width="0.127" layer="21"/>
<text x="-17.78" y="0" size="1.27" layer="21" font="vector">&gt;NAME</text>
<text x="-17.78" y="-2.54" size="1.27" layer="21" font="vector">&gt;VALUE</text>
<circle x="0" y="0" radius="1.79605" width="0.127" layer="21"/>
<text x="3.81" y="-1.27" size="0.8128" layer="21" font="vector" rot="R90">Reset</text>
<text x="-20.32" y="-6.35" size="1.016" layer="21" font="vector">1</text>
<text x="-17.78" y="3.81" size="0.6096" layer="21" font="vector" rot="R180">Mini-B USB</text>
<wire x1="19.05" y1="3.81" x2="13.97" y2="3.81" width="0.127" layer="21"/>
<wire x1="13.97" y1="3.81" x2="13.97" y2="-3.81" width="0.127" layer="21"/>
<wire x1="13.97" y1="-3.81" x2="19.05" y2="-3.81" width="0.127" layer="21"/>
<circle x="17.78" y="-2.54" radius="0.8" width="0.127" layer="21"/>
<circle x="17.78" y="0" radius="0.8" width="0.127" layer="21"/>
<circle x="17.78" y="2.54" radius="0.8" width="0.127" layer="21"/>
<circle x="15.24" y="2.54" radius="0.8" width="0.127" layer="21"/>
<circle x="17.78" y="0" radius="0.8" width="0.127" layer="21"/>
<circle x="15.24" y="0" radius="0.8" width="0.127" layer="21"/>
<circle x="15.24" y="-2.54" radius="0.8" width="0.127" layer="21"/>
<text x="12.7" y="1.27" size="0.8128" layer="21" font="vector" rot="SR270">ICSP</text>
</package>
</packages>
<symbols>
<symbol name="ARDUINO-NANO-V3">
<wire x1="-12.7" y1="22.86" x2="12.7" y2="22.86" width="0.254" layer="94"/>
<wire x1="12.7" y1="22.86" x2="12.7" y2="-27.94" width="0.254" layer="94"/>
<wire x1="12.7" y1="-27.94" x2="-12.7" y2="-27.94" width="0.254" layer="94"/>
<wire x1="-12.7" y1="-27.94" x2="-12.7" y2="22.86" width="0.254" layer="94"/>
<pin name="A0" x="-17.78" y="10.16" visible="pin" length="middle"/>
<pin name="A1" x="-17.78" y="7.62" visible="pin" length="middle"/>
<pin name="A2" x="-17.78" y="5.08" visible="pin" length="middle"/>
<pin name="A3" x="-17.78" y="2.54" visible="pin" length="middle"/>
<pin name="A4(SDA)" x="-17.78" y="0" visible="pin" length="middle"/>
<pin name="A5(SCL)" x="-17.78" y="-2.54" visible="pin" length="middle"/>
<pin name="A6" x="-17.78" y="-5.08" visible="pin" length="middle"/>
<pin name="A7" x="-17.78" y="-7.62" visible="pin" length="middle"/>
<pin name="(RXD)D0" x="17.78" y="20.32" visible="pin" length="middle" rot="R180"/>
<pin name="(TXD)D1" x="17.78" y="17.78" visible="pin" length="middle" rot="R180"/>
<pin name="(INT0)D2" x="17.78" y="15.24" visible="pin" length="middle" rot="R180"/>
<pin name="(PWM)D3" x="17.78" y="12.7" visible="pin" length="middle" rot="R180"/>
<pin name="(T0)D4" x="17.78" y="10.16" visible="pin" length="middle" rot="R180"/>
<pin name="(PWM)D5" x="17.78" y="7.62" visible="pin" length="middle" rot="R180"/>
<pin name="(PWM)D6" x="17.78" y="5.08" visible="pin" length="middle" rot="R180"/>
<pin name="D7" x="17.78" y="2.54" visible="pin" length="middle" rot="R180"/>
<pin name="D8" x="17.78" y="-2.54" visible="pin" length="middle" rot="R180"/>
<pin name="(PWM)D9" x="17.78" y="-5.08" visible="pin" length="middle" rot="R180"/>
<pin name="(SS)D10" x="17.78" y="-10.16" visible="pin" length="middle" rot="R180"/>
<pin name="(MOSI)D11" x="17.78" y="-12.7" visible="pin" length="middle" rot="R180"/>
<pin name="(MISO)D12" x="17.78" y="-15.24" visible="pin" length="middle" rot="R180"/>
<pin name="(SCK)D13" x="17.78" y="-17.78" visible="pin" length="middle" rot="R180"/>
<pin name="!RST@13" x="-17.78" y="-17.78" visible="pin" length="middle" function="dot"/>
<pin name="!RST@18" x="-17.78" y="-20.32" visible="pin" length="middle" function="dot"/>
<pin name="GND@14" x="-17.78" y="-25.4" visible="pin" length="middle"/>
<pin name="GND@19" x="17.78" y="-25.4" visible="pin" length="middle" rot="R180"/>
<pin name="VIN" x="-17.78" y="20.32" visible="pin" length="middle"/>
<pin name="5V0" x="-17.78" y="17.78" visible="pin" length="middle"/>
<pin name="3V3" x="-17.78" y="15.24" visible="pin" length="middle"/>
<pin name="AREF" x="-17.78" y="-12.7" visible="pin" length="middle"/>
<text x="-12.7" y="26.67" size="1.778" layer="95">&gt;NAME</text>
<text x="-12.7" y="24.13" size="1.778" layer="96">&gt;VALUE</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="ARDUINO_NANO_V3">
<gates>
<gate name="G$1" symbol="ARDUINO-NANO-V3" x="0" y="0"/>
</gates>
<devices>
<device name="" package="ARDUINO_NANO">
<connects>
<connect gate="G$1" pin="!RST@13" pad="13"/>
<connect gate="G$1" pin="!RST@18" pad="18"/>
<connect gate="G$1" pin="(INT0)D2" pad="20"/>
<connect gate="G$1" pin="(MISO)D12" pad="30"/>
<connect gate="G$1" pin="(MOSI)D11" pad="29"/>
<connect gate="G$1" pin="(PWM)D3" pad="21"/>
<connect gate="G$1" pin="(PWM)D5" pad="23"/>
<connect gate="G$1" pin="(PWM)D6" pad="24"/>
<connect gate="G$1" pin="(PWM)D9" pad="27"/>
<connect gate="G$1" pin="(RXD)D0" pad="17"/>
<connect gate="G$1" pin="(SCK)D13" pad="1"/>
<connect gate="G$1" pin="(SS)D10" pad="28"/>
<connect gate="G$1" pin="(T0)D4" pad="22"/>
<connect gate="G$1" pin="(TXD)D1" pad="16"/>
<connect gate="G$1" pin="3V3" pad="2"/>
<connect gate="G$1" pin="5V0" pad="12"/>
<connect gate="G$1" pin="A0" pad="4"/>
<connect gate="G$1" pin="A1" pad="5"/>
<connect gate="G$1" pin="A2" pad="6"/>
<connect gate="G$1" pin="A3" pad="7"/>
<connect gate="G$1" pin="A4(SDA)" pad="8"/>
<connect gate="G$1" pin="A5(SCL)" pad="9"/>
<connect gate="G$1" pin="A6" pad="10"/>
<connect gate="G$1" pin="A7" pad="11"/>
<connect gate="G$1" pin="AREF" pad="3"/>
<connect gate="G$1" pin="D7" pad="25"/>
<connect gate="G$1" pin="D8" pad="26"/>
<connect gate="G$1" pin="GND@14" pad="14"/>
<connect gate="G$1" pin="GND@19" pad="19"/>
<connect gate="G$1" pin="VIN" pad="15"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply1" urn="urn:adsk.eagle:library:371">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
 GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
 Please keep in mind, that these devices are necessary for the
 automatic wiring of the supply signals.&lt;p&gt;
 The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
 In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
 &lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="GND" urn="urn:adsk.eagle:symbol:26925/1" library_version="1">
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GND" urn="urn:adsk.eagle:component:26954/1" prefix="GND" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply2" urn="urn:adsk.eagle:library:372">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
Please keep in mind, that these devices are necessary for the
automatic wiring of the supply signals.&lt;p&gt;
The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="+05V" urn="urn:adsk.eagle:symbol:26987/1" library_version="2">
<wire x1="-0.635" y1="1.27" x2="0.635" y2="1.27" width="0.1524" layer="94"/>
<wire x1="0" y1="0.635" x2="0" y2="1.905" width="0.1524" layer="94"/>
<circle x="0" y="1.27" radius="1.27" width="0.254" layer="94"/>
<text x="-1.905" y="3.175" size="1.778" layer="96">&gt;VALUE</text>
<pin name="+5V" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="+5V" urn="urn:adsk.eagle:component:27032/1" prefix="SUPPLY" library_version="2">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="+5V" symbol="+05V" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="ngspice-simulation" urn="urn:adsk.eagle:library:527439">
<description>SPICE compatible library parts</description>
<packages>
</packages>
<symbols>
<symbol name="C" urn="urn:adsk.eagle:symbol:527449/4" library_version="18">
<description>Capacitor</description>
<rectangle x1="-2.032" y1="-2.032" x2="2.032" y2="-1.524" layer="94"/>
<rectangle x1="-2.032" y1="-1.016" x2="2.032" y2="-0.508" layer="94"/>
<wire x1="0" y1="0" x2="0" y2="-0.508" width="0.1524" layer="94"/>
<wire x1="0" y1="-2.54" x2="0" y2="-2.032" width="0.1524" layer="94"/>
<pin name="1" x="0" y="2.54" visible="off" length="short" direction="pas" swaplevel="1" rot="R270"/>
<pin name="2" x="0" y="-5.08" visible="off" length="short" direction="pas" swaplevel="1" rot="R90"/>
<text x="2.54" y="2.54" size="1.778" layer="95">&gt;NAME</text>
<text x="2.54" y="-2.54" size="1.778" layer="97">&gt;SPICEMODEL</text>
<text x="2.54" y="0" size="1.778" layer="96">&gt;VALUE</text>
<text x="2.54" y="-5.08" size="1.778" layer="97">&gt;SPICEEXTRA</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="C" urn="urn:adsk.eagle:component:527468/6" prefix="C" uservalue="yes" library_version="18">
<description>CAPACITOR</description>
<gates>
<gate name="G$1" symbol="C" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name="">
<attribute name="_EXTERNAL_" value="" constant="no"/>
</technology>
</technologies>
</device>
</devices>
<spice>
<pinmapping spiceprefix="C">
<pinmap gate="G$1" pin="1" pinorder="1"/>
<pinmap gate="G$1" pin="2" pinorder="2"/>
</pinmapping>
</spice>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="UK1" library="Arduino_DWD" deviceset="ARDUINO_NANO_V3" device=""/>
<part name="UK2" library="Arduino_DWD" deviceset="ARDUINO_NANO_V3" device=""/>
<part name="GND1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="SUPPLY1" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="+5V" device=""/>
<part name="SUPPLY2" library="supply2" library_urn="urn:adsk.eagle:library:372" deviceset="+5V" device=""/>
<part name="C1" library="ngspice-simulation" library_urn="urn:adsk.eagle:library:527439" deviceset="C" device="" value="10uF"/>
</parts>
<sheets>
<sheet>
<plain>
<wire x1="-25.4" y1="71.12" x2="-25.4" y2="-15.24" width="0.508" layer="97" style="longdash"/>
<wire x1="-25.4" y1="-15.24" x2="35.56" y2="-15.24" width="0.508" layer="97" style="longdash"/>
<wire x1="35.56" y1="-15.24" x2="35.56" y2="71.12" width="0.508" layer="97" style="longdash"/>
<wire x1="35.56" y1="71.12" x2="-25.4" y2="71.12" width="0.508" layer="97" style="longdash"/>
<wire x1="63.5" y1="71.12" x2="63.5" y2="-15.24" width="0.508" layer="97" style="longdash"/>
<wire x1="63.5" y1="-15.24" x2="124.46" y2="-15.24" width="0.508" layer="97" style="longdash"/>
<wire x1="124.46" y1="-15.24" x2="124.46" y2="71.12" width="0.508" layer="97" style="longdash"/>
<wire x1="124.46" y1="71.12" x2="63.5" y2="71.12" width="0.508" layer="97" style="longdash"/>
<text x="-10.16" y="66.04" size="2.54" layer="97">Arduino as ISP programmer</text>
<text x="66.04" y="66.04" size="2.54" layer="97">Arduino as target</text>
</plain>
<instances>
<instance part="UK1" gate="G$1" x="12.7" y="27.94" smashed="yes">
<attribute name="NAME" x="0" y="54.61" size="1.778" layer="95"/>
<attribute name="VALUE" x="0" y="52.07" size="1.778" layer="96"/>
</instance>
<instance part="UK2" gate="G$1" x="88.9" y="27.94" smashed="yes" rot="MR0">
<attribute name="NAME" x="101.6" y="54.61" size="1.778" layer="95" rot="MR0"/>
<attribute name="VALUE" x="101.6" y="52.07" size="1.778" layer="96" rot="MR0"/>
</instance>
<instance part="GND1" gate="1" x="-5.08" y="-7.62" smashed="yes">
<attribute name="VALUE" x="-7.62" y="-10.16" size="1.778" layer="96"/>
</instance>
<instance part="GND2" gate="1" x="116.84" y="-7.62" smashed="yes">
<attribute name="VALUE" x="114.3" y="-10.16" size="1.778" layer="96"/>
</instance>
<instance part="SUPPLY1" gate="+5V" x="-12.7" y="58.42" smashed="yes">
<attribute name="VALUE" x="-14.605" y="61.595" size="1.778" layer="96"/>
</instance>
<instance part="SUPPLY2" gate="+5V" x="114.3" y="58.42" smashed="yes">
<attribute name="VALUE" x="112.395" y="61.595" size="1.778" layer="96"/>
</instance>
<instance part="C1" gate="G$1" x="-12.7" y="2.54" smashed="yes" rot="R180">
<attribute name="NAME" x="-15.24" y="5.08" size="1.778" layer="95" rot="R180"/>
<attribute name="VALUE" x="-15.24" y="2.54" size="1.778" layer="96" rot="R180"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="N$1" class="0">
<segment>
<pinref part="C1" gate="G$1" pin="2"/>
<pinref part="UK1" gate="G$1" pin="!RST@18"/>
<wire x1="-12.7" y1="7.62" x2="-5.08" y2="7.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="C1" gate="G$1" pin="1"/>
<wire x1="-12.7" y1="0" x2="-12.7" y2="-2.54" width="0.1524" layer="91"/>
<wire x1="-12.7" y1="-2.54" x2="-5.08" y2="-2.54" width="0.1524" layer="91"/>
<pinref part="UK1" gate="G$1" pin="GND@14"/>
<wire x1="-5.08" y1="-2.54" x2="-5.08" y2="2.54" width="0.1524" layer="91"/>
<pinref part="GND1" gate="1" pin="GND"/>
<wire x1="-5.08" y1="-5.08" x2="-5.08" y2="-2.54" width="0.1524" layer="91"/>
<junction x="-5.08" y="-2.54"/>
</segment>
<segment>
<pinref part="UK2" gate="G$1" pin="GND@14"/>
<pinref part="GND2" gate="1" pin="GND"/>
<wire x1="106.68" y1="2.54" x2="116.84" y2="2.54" width="0.1524" layer="91"/>
<wire x1="116.84" y1="2.54" x2="116.84" y2="-5.08" width="0.1524" layer="91"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<pinref part="SUPPLY2" gate="+5V" pin="+5V"/>
<pinref part="UK2" gate="G$1" pin="VIN"/>
<wire x1="114.3" y1="55.88" x2="114.3" y2="48.26" width="0.1524" layer="91"/>
<wire x1="114.3" y1="48.26" x2="106.68" y2="48.26" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="SUPPLY1" gate="+5V" pin="+5V"/>
<pinref part="UK1" gate="G$1" pin="VIN"/>
<wire x1="-12.7" y1="55.88" x2="-12.7" y2="48.26" width="0.1524" layer="91"/>
<wire x1="-12.7" y1="48.26" x2="-5.08" y2="48.26" width="0.1524" layer="91"/>
</segment>
</net>
<net name="MOSI" class="0">
<segment>
<pinref part="UK1" gate="G$1" pin="(MOSI)D11"/>
<pinref part="UK2" gate="G$1" pin="(MOSI)D11"/>
<wire x1="30.48" y1="15.24" x2="71.12" y2="15.24" width="0.1524" layer="91"/>
<label x="45.72" y="15.24" size="1.778" layer="95"/>
</segment>
</net>
<net name="MISO" class="0">
<segment>
<pinref part="UK1" gate="G$1" pin="(MISO)D12"/>
<pinref part="UK2" gate="G$1" pin="(MISO)D12"/>
<wire x1="30.48" y1="12.7" x2="71.12" y2="12.7" width="0.1524" layer="91"/>
<label x="45.72" y="12.7" size="1.778" layer="95"/>
</segment>
</net>
<net name="SCK" class="0">
<segment>
<pinref part="UK1" gate="G$1" pin="(SCK)D13"/>
<pinref part="UK2" gate="G$1" pin="(SCK)D13"/>
<wire x1="30.48" y1="10.16" x2="71.12" y2="10.16" width="0.1524" layer="91"/>
<label x="45.72" y="10.16" size="1.778" layer="95"/>
</segment>
</net>
<net name="!RST" class="0">
<segment>
<pinref part="UK1" gate="G$1" pin="(SS)D10"/>
<wire x1="30.48" y1="17.78" x2="40.64" y2="17.78" width="0.1524" layer="91"/>
<wire x1="40.64" y1="17.78" x2="40.64" y2="-2.54" width="0.1524" layer="91"/>
<wire x1="40.64" y1="-2.54" x2="114.3" y2="-2.54" width="0.1524" layer="91"/>
<wire x1="114.3" y1="-2.54" x2="114.3" y2="7.62" width="0.1524" layer="91"/>
<pinref part="UK2" gate="G$1" pin="!RST@18"/>
<wire x1="114.3" y1="7.62" x2="106.68" y2="7.62" width="0.1524" layer="91"/>
<label x="45.72" y="-2.54" size="1.778" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, EAGLE supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports URNs for individual library
assets (packages, symbols, and devices). The URNs of those assets
will not be understood (or retained) with this version.
</note>
<note version="8.4" severity="warning">
Since Version 8.4, EAGLE supports properties for SPICE simulation. 
Probes in schematics and SPICE mapping objects found in parts and library devices
will not be understood with this version. Update EAGLE to the latest version
for full support of SPICE simulation. 
</note>
</compatibility>
</eagle>
