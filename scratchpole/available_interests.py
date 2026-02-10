from dataclasses import dataclass

@dataclass(frozen=True)
class Interest:
    label: str
    regex: str

interests = {
    'filament.used.mm': Interest('Filament used (mm)', r'; filament used \[mm] = (.*)'),
    'filament.used.cm3': Interest('Filament used (cm^3)', r'; filament used \[cm3] = (.*)'),
    'filament.used.g': Interest('Filament used (g)', r'; filament used \[g] = (.*)'),
    'filament.used.cost': Interest('Filament cost ($)', r'; filament cost = (.*)'),
    'filament.used.wipe_tower': Interest('Filament used (In wipe tower, g)', r'; total filament used for wipe tower \[g] = (.*)'),
    'filament.used.total_g': Interest('Filament used (Total, g)', r'; total filament used \[g] = (.*)'),
    'filament.used.total_cost': Interest('Filament cost (Total, $)', '; total filament cost = (.*)'),

    'time.normal.estimated': Interest('Printing time (Estimated, Normal mode)', r'; estimated printing time \(normal mode\) = (.*)'),
    'time.silent.estimated': Interest('Printing time (Estimated, Silent mode)', r'; estimated printing time \(silent mode\) = (.*)'),
    'time.normal.first_layer': Interest('Printing time (First layer, Normal mode)', r'; estimated first layer printing time \(normal mode\) = (.*)'),
    'time.silent.first_layer': Interest('Printing time (First layer, Silent mode)', r'; estimated first layer printing time \(silent mode\) = (.*)'),
}