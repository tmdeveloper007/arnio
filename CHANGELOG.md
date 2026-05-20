# Changelog

## [1.10.0](https://github.com/tmdeveloper007/arnio/compare/v1.14.0...v1.10.0) (2026-05-20)


### Features

* add __getitem__ to ArFrame for column access ([78dd66c](https://github.com/tmdeveloper007/arnio/commit/78dd66c1053f6c04bc61c35a9b81f016b37ac73a))
* add ArFrame __contains__ support ([2e63c39](https://github.com/tmdeveloper007/arnio/commit/2e63c396730caef6e6b2d8d238c046ea22d889bc))
* add ArFrame preview method ([814102e](https://github.com/tmdeveloper007/arnio/commit/814102e35b153cf75b3a759a5e33867edfe03321))
* add ArFrame select_columns helper ([fff406d](https://github.com/tmdeveloper007/arnio/commit/fff406d9a10943cb6f2bd76d32240933da90ed51))
* add ArFrame.select_dtypes() for type-based column selection ([1c56e23](https://github.com/tmdeveloper007/arnio/commit/1c56e2369b3abf3fc80e2448f912fd3194b9c63b))
* add benchmark regression reporting ([#554](https://github.com/tmdeveloper007/arnio/issues/554)) ([83b9ee5](https://github.com/tmdeveloper007/arnio/commit/83b9ee5c8cf75477ebb476f1fb3f13654eceab3a))
* add bounded profiling sample_size validation ([1e31269](https://github.com/tmdeveloper007/arnio/commit/1e3126986bdc21e128fc734a71a77aa7f242441a))
* add clip_numeric cleaning helper ([4022449](https://github.com/tmdeveloper007/arnio/commit/4022449c7bbe5e31c94e756ff29a36b4c274a232))
* add column existence validation helper ([517d1e0](https://github.com/tmdeveloper007/arnio/commit/517d1e07d3b19252027ecdfac23d17b19e0aa793))
* add composite uniqueness validation support ([#495](https://github.com/tmdeveloper007/arnio/issues/495)) ([8b11e19](https://github.com/tmdeveloper007/arnio/commit/8b11e19180b97fde1c380857e702d78dc7df8fc8))
* add conditional required validation ([34c75a2](https://github.com/tmdeveloper007/arnio/commit/34c75a20efb0e06acc2d036296e25eb484b090df))
* add confidence metadata to cleaning suggestions ([2a78f8a](https://github.com/tmdeveloper007/arnio/commit/2a78f8a09d36147ce58f554a153340a60cb888fd))
* add CountryCode schema validator ([#487](https://github.com/tmdeveloper007/arnio/issues/487)) ([14a77e5](https://github.com/tmdeveloper007/arnio/commit/14a77e532409bffc0fdef85fbbbaaa798782dde7))
* add CSV delimiter sniffing helper (fixes [#127](https://github.com/tmdeveloper007/arnio/issues/127)) ([#801](https://github.com/tmdeveloper007/arnio/issues/801)) ([cad39d9](https://github.com/tmdeveloper007/arnio/commit/cad39d94501e6684dc364c246ffa9f867604bce6))
* add CurrencyCode schema validation ([fdfda2b](https://github.com/tmdeveloper007/arnio/commit/fdfda2b2774fcb3b45871314186ba84cf769b87d)), closes [#204](https://github.com/tmdeveloper007/arnio/issues/204)
* add data quality engine ([6053ab9](https://github.com/tmdeveloper007/arnio/commit/6053ab93fa29b706a20f5fd8d905f046fedb36c5))
* add data quality engine ([f8abb2f](https://github.com/tmdeveloper007/arnio/commit/f8abb2f8202e9d1fa394a2e1e97576f003d113b0))
* add DataQualityReport markdown export ([20b2f68](https://github.com/tmdeveloper007/arnio/commit/20b2f68c0fb29516366ca753327896a8eaba6392))
* add Date schema field ([c52ac18](https://github.com/tmdeveloper007/arnio/commit/c52ac18fff979ef5b49b04a00b8d6d8faa4b933d))
* add DateTime schema field ([05c26be](https://github.com/tmdeveloper007/arnio/commit/05c26bebf1cf79bbdbb98157dba1618c61abd08e))
* add Decimal conversion policy ([97b1a1c](https://github.com/tmdeveloper007/arnio/commit/97b1a1cc0ede5fbf0aef4176339fa4b2cf4cfed0))
* add drop constant columns ([#357](https://github.com/tmdeveloper007/arnio/issues/357)) ([3e13d3d](https://github.com/tmdeveloper007/arnio/commit/3e13d3d576add9fd8113cdf185ca08e61e75c4ee))
* add drop_columns cleaning primitive ([#769](https://github.com/tmdeveloper007/arnio/issues/769)) ([2616c66](https://github.com/tmdeveloper007/arnio/commit/2616c6691563c037cfbea0bffc140c5ed4ded05e))
* add drop_columns_matching cleaning step ([#743](https://github.com/tmdeveloper007/arnio/issues/743)) ([5db2fd1](https://github.com/tmdeveloper007/arnio/commit/5db2fd1ba8b040986eee08bc6fa27da1e5ccc473))
* add explain mode for auto_clean ([#692](https://github.com/tmdeveloper007/arnio/issues/692)) ([24036fa](https://github.com/tmdeveloper007/arnio/commit/24036fa259804ec504e36d2f94d5f4e4a3cac573))
* add filter_rows pipeline step ([#288](https://github.com/tmdeveloper007/arnio/issues/288)) ([a3b7386](https://github.com/tmdeveloper007/arnio/commit/a3b7386e75bc45c9a7fde403ea373334ef528f75))
* add head() and tail() methods to ArFrame ([#565](https://github.com/tmdeveloper007/arnio/issues/565)) ([f254add](https://github.com/tmdeveloper007/arnio/commit/f254add98cecb78404a99b01a9290fe96b2adb53))
* add is_empty convenience property to ArFrame ([37df94d](https://github.com/tmdeveloper007/arnio/commit/37df94d0e4f782fc4510ea8ad179960f51c0fc7d))
* add keep_rows_with_nulls pipeline step ([37dde00](https://github.com/tmdeveloper007/arnio/commit/37dde009d3899e3647183f34209f171afca11f31))
* add normalize_unicode cleaning step ([c8c7c40](https://github.com/tmdeveloper007/arnio/commit/c8c7c40c9172e83d289b25e2e4b797efd78cd26a))
* add numeric quantiles to profile reports ([3934520](https://github.com/tmdeveloper007/arnio/commit/3934520c61abc4fe038b973b8a999bb00520ba74))
* add optional pipeline timing metadata ([7da0bae](https://github.com/tmdeveloper007/arnio/commit/7da0bae28b0cd691781c47f572237dd629bfc2bc)), closes [#162](https://github.com/tmdeveloper007/arnio/issues/162)
* add pandas integration direction ([#399](https://github.com/tmdeveloper007/arnio/issues/399)) ([22f9b58](https://github.com/tmdeveloper007/arnio/commit/22f9b58458383549d97d81ff7828b7a047063525))
* add parse_bool_strings pipeline step ([bc6e53d](https://github.com/tmdeveloper007/arnio/commit/bc6e53d6cbf73c02bcbd81f828a6c085ed928797)), closes [#150](https://github.com/tmdeveloper007/arnio/issues/150)
* add PhoneNumber schema validator ([#745](https://github.com/tmdeveloper007/arnio/issues/745)) ([21717d0](https://github.com/tmdeveloper007/arnio/commit/21717d07e5bc03098809b1312d51b919c74fd123))
* add pipeline step registry introspection ([8178f0a](https://github.com/tmdeveloper007/arnio/commit/8178f0a995bc65f425189647ef4f8d59cf4e4537)), closes [#157](https://github.com/tmdeveloper007/arnio/issues/157)
* add quality sample redaction ([#555](https://github.com/tmdeveloper007/arnio/issues/555)) ([daece46](https://github.com/tmdeveloper007/arnio/commit/daece46037eab5bc924d8e61b4111dc659301ed9))
* add quality score components ([130ad70](https://github.com/tmdeveloper007/arnio/commit/130ad70075757051f1a49c8a0d9d9efb7e5a94de))
* add refactor task issue template ([#334](https://github.com/tmdeveloper007/arnio/issues/334)) ([6690947](https://github.com/tmdeveloper007/arnio/commit/6690947bcada6dc825853036a11ad2310acdd4e4))
* add Regex field validator to schema ([#537](https://github.com/tmdeveloper007/arnio/issues/537)) ([70b1839](https://github.com/tmdeveloper007/arnio/commit/70b18395066c424e143a1a8eb034f3f200d92333))
* add replace_values pipeline step ([#348](https://github.com/tmdeveloper007/arnio/issues/348)) ([02b297c](https://github.com/tmdeveloper007/arnio/commit/02b297c0d60fdb4417e801f2f28db92f50441a4c))
* add round_numeric_columns cleaning helper ([61cd110](https://github.com/tmdeveloper007/arnio/commit/61cd1105e60c6daa38d34ef602f3f9fac28de7ea))
* add safe_divide_columns cleaning step ([80e4a65](https://github.com/tmdeveloper007/arnio/commit/80e4a654d81a1bd95e96b1f5ec83f5f82deff590))
* add sample_size to scan_csv ([9f72698](https://github.com/tmdeveloper007/arnio/commit/9f726987a08b57fc8fa5d6d611e59f6c444a6232))
* add schema JSON serialization ([7c919a1](https://github.com/tmdeveloper007/arnio/commit/7c919a1f48453b37975c1e964d72c90c1b86e6fc))
* add scikit-learn ArnioCleaner transformer ([610a39f](https://github.com/tmdeveloper007/arnio/commit/610a39fe5ab4a02db2ad7f9c3223896cdf263db5))
* add scikit-learn ArnioCleaner transformer ([9788d28](https://github.com/tmdeveloper007/arnio/commit/9788d28fb24ceeca40139ea716996a8f5a330249))
* add standardize_missing_tokens step ([b2bd596](https://github.com/tmdeveloper007/arnio/commit/b2bd596e03c5a3e3143093116ed7f58b557ef84b))
* add string length statistics to quality profile (resolves [#174](https://github.com/tmdeveloper007/arnio/issues/174)) ([#550](https://github.com/tmdeveloper007/arnio/issues/550)) ([98d1bf3](https://github.com/tmdeveloper007/arnio/commit/98d1bf34a9b175610efbb360d034ce0663a8a547))
* add strip_whitespace allocation benchmark ([e2ff584](https://github.com/tmdeveloper007/arnio/commit/e2ff58416125fe1eae4bef4c204cc52fb248fb86))
* add thousands separator parsing ([7ffe50c](https://github.com/tmdeveloper007/arnio/commit/7ffe50cfd669f96cbdc32248fd425d34eb9f1e83))
* add to_pandas copy option ([1746fe1](https://github.com/tmdeveloper007/arnio/commit/1746fe15d5c399d649fff9561a7a02bea147c4de))
* add top_values summary for categorical columns ([f593f94](https://github.com/tmdeveloper007/arnio/commit/f593f94cf331180f29516d1afc217c106a96ad8b))
* add trim_column_names to strip whitespace from column names (Fixes [#138](https://github.com/tmdeveloper007/arnio/issues/138)) ([d4f42c9](https://github.com/tmdeveloper007/arnio/commit/d4f42c9a343f52a74b7da23ae8f830c8687d8fda))
* add trim_headers CSV option ([022460e](https://github.com/tmdeveloper007/arnio/commit/022460e1fa7e9510960a789aa38f835731dec700))
* add validation summary counts ([#444](https://github.com/tmdeveloper007/arnio/issues/444)) ([6575491](https://github.com/tmdeveloper007/arnio/commit/657549174aaca524ce77f169a7e7b3a7b230cba0))
* add ValidationResult.raise_for_errors ([4c34bf6](https://github.com/tmdeveloper007/arnio/commit/4c34bf60f70fa2f5c3183a1598066c4f470003c1))
* add ValidationResult.to_markdown ([168e525](https://github.com/tmdeveloper007/arnio/commit/168e525409ce3a8d60f972dadacfaab01c4cafa8))
* add write_csv via C++ backend ([2a62edc](https://github.com/tmdeveloper007/arnio/commit/2a62edc94108f59fa4894ae88cf266000bb1626d))
* **convert:** preserve DataFrame attrs roundtrip ([4018f27](https://github.com/tmdeveloper007/arnio/commit/4018f27f76dbb021591b4aa6844e2c130887dceb))
* **csv:** add chunked streaming CSV reader ([8032a81](https://github.com/tmdeveloper007/arnio/commit/8032a81f3022652df3027bd93fc1ebc0a234c224))
* **csv:** add strict and permissive parser modes ([9cf1e07](https://github.com/tmdeveloper007/arnio/commit/9cf1e07de25888a90dd3cd68c7f1c1a46e3962f6)), closes [#132](https://github.com/tmdeveloper007/arnio/issues/132)
* enhance pull request template with media and performance sections ([#336](https://github.com/tmdeveloper007/arnio/issues/336)) ([99b588b](https://github.com/tmdeveloper007/arnio/commit/99b588b62910a68b83abdb39455c0d59de6bba56))
* enrich pipeline execution metadata ([348104a](https://github.com/tmdeveloper007/arnio/commit/348104a4159437f77100106033916afd0f39c2b8)), closes [#166](https://github.com/tmdeveloper007/arnio/issues/166)
* expose built-in pipeline step signatures ([25cc277](https://github.com/tmdeveloper007/arnio/commit/25cc277b911b3caad0925df392c581aa03796f8d)), closes [#170](https://github.com/tmdeveloper007/arnio/issues/170)
* implement configurable missing data values handling ([#783](https://github.com/tmdeveloper007/arnio/issues/783)) ([765875c](https://github.com/tmdeveloper007/arnio/commit/765875c75b89da0e641be8b927dfe26935d3482b))
* implement HTML export for DataQualityReport ([#685](https://github.com/tmdeveloper007/arnio/issues/685)) ([6296568](https://github.com/tmdeveloper007/arnio/commit/629656896efb18c33f1949f047738b2dbe48972b))
* initial implementation of C++ core and Python API ([9b9b74c](https://github.com/tmdeveloper007/arnio/commit/9b9b74c86feed2208dfaa26547400321a92e424c))
* initial implementation of C++ core and Python API ([20515df](https://github.com/tmdeveloper007/arnio/commit/20515df85e598a96a26ce3230e46d910fe4357f1))
* **io:** add read_jsonl() for JSON Lines support ([095b89d](https://github.com/tmdeveloper007/arnio/commit/095b89d52d57c6c9be528f7f0d6b4d10462d8383)), closes [#634](https://github.com/tmdeveloper007/arnio/issues/634)
* **io:** support text file-like inputs in read_csv ([4549170](https://github.com/tmdeveloper007/arnio/commit/4549170986409d3dc3289506b377f10d884e2d78))
* notebook-friendly DataQualityReport dashboard ([#737](https://github.com/tmdeveloper007/arnio/issues/737)) ([9e16e18](https://github.com/tmdeveloper007/arnio/commit/9e16e187be8b20d163660c12c6ddca23133dbbbb))
* phase 1 - normalize_case fix, to_pandas rewrite, Python registry ([344533a](https://github.com/tmdeveloper007/arnio/commit/344533a43a5a9888cab4b5d8eff9bf47f277e8db))
* phase 1 - normalize_case fix, to_pandas rewrite, Python registry ([66b60fb](https://github.com/tmdeveloper007/arnio/commit/66b60fb32dfff3c8841bc3a587960a8a85d9a1f5))
* **pipeline:** add dry_run validation mode ([2768b4a](https://github.com/tmdeveloper007/arnio/commit/2768b4aa265fec2c4e5a6df60db418df072cabef))
* **quality:** add compare_profiles helper ([a83c860](https://github.com/tmdeveloper007/arnio/commit/a83c860ec5ff05c7d3f33a526550e93f456d2a49)), closes [#185](https://github.com/tmdeveloper007/arnio/issues/185)
* **quality:** add drift gate checks ([#735](https://github.com/tmdeveloper007/arnio/issues/735)) ([7029151](https://github.com/tmdeveloper007/arnio/commit/7029151268b8ae1b285e1d2145192c93be8d3879))
* **quality:** add email and URL validity ratios to column profiles ([#176](https://github.com/tmdeveloper007/arnio/issues/176)) ([#808](https://github.com/tmdeveloper007/arnio/issues/808)) ([e4a96f9](https://github.com/tmdeveloper007/arnio/commit/e4a96f9e1a5c64e236ad0d85dd0ba6b5cdf10d49))
* register combine_columns as pipeline step and add test ([beaf402](https://github.com/tmdeveloper007/arnio/commit/beaf4022ac7dc70cb370d387769fc033beb4454d))
* register combine_columns as pipeline step and add test ([c209125](https://github.com/tmdeveloper007/arnio/commit/c2091255286ca66e6b6e54f4f9dcdc304e8fa949))
* **schema:** add cross-field validation rules parameter ([#651](https://github.com/tmdeveloper007/arnio/issues/651)) ([36d0545](https://github.com/tmdeveloper007/arnio/commit/36d054549166542c5401f7a057df25f8a4ab7095)), closes [#196](https://github.com/tmdeveloper007/arnio/issues/196)
* **schema:** add schema diff helper ([fe82072](https://github.com/tmdeveloper007/arnio/commit/fe820726cef88ad6ba702decd46bbe29fbcd8999)), closes [#209](https://github.com/tmdeveloper007/arnio/issues/209)
* **schema:** add warning severity support ([58929c6](https://github.com/tmdeveloper007/arnio/commit/58929c6047d11800e095cd4e3cbfc95d1f379c4b)), closes [#192](https://github.com/tmdeveloper007/arnio/issues/192)
* **schema:** bootstrap schema from quality report ([#529](https://github.com/tmdeveloper007/arnio/issues/529)) ([498d8d4](https://github.com/tmdeveloper007/arnio/commit/498d8d42deb13119a6f48d59a79562ed68f4ddec))
* support namespaced pipeline steps ([57dec91](https://github.com/tmdeveloper007/arnio/commit/57dec91f31efbac2f5778af56b9b7afbd3836081)), closes [#168](https://github.com/tmdeveloper007/arnio/issues/168)
* truncate long ArFrame column names in display ([#566](https://github.com/tmdeveloper007/arnio/issues/566)) ([66bdc0c](https://github.com/tmdeveloper007/arnio/commit/66bdc0c9310048ca979389ead3111fcc7e6d8054))
* wrap custom pipeline step errors ([72ddda1](https://github.com/tmdeveloper007/arnio/commit/72ddda1a9ebf7b32619933e7d177f63e4a861ede))


### Bug Fixes

* 52: Remove public set_dtype() and add assert_type_consistency ([4adfc6c](https://github.com/tmdeveloper007/arnio/commit/4adfc6c96456fa0263918fa2ce54cabfcaa2c0c8))
* 52: Remove public set_dtype() and add assert_type_consistency ([9d041c7](https://github.com/tmdeveloper007/arnio/commit/9d041c7ee712262bfce74207df8301ded59ce6bb))
* add YAML validation for GitHub workflow files ([0c666ca](https://github.com/tmdeveloper007/arnio/commit/0c666caa0ce937d70fdffc58dee2e8ba12338412))
* address maintainer review (sklearn constraints, copy behavior, tests) ([37da442](https://github.com/tmdeveloper007/arnio/commit/37da442c4f4bdf8f73911b9bd60fbebcf49568c1))
* align round_numeric_columns subset errors ([#774](https://github.com/tmdeveloper007/arnio/issues/774)) ([f9a7a4b](https://github.com/tmdeveloper007/arnio/commit/f9a7a4ba54d635d95d2f5ea2ccfe01bb77412e9e))
* allow encoded csv nul handling ([5796a35](https://github.com/tmdeveloper007/arnio/commit/5796a35a32aff5a5d889a72deee255232c527929)), closes [#422](https://github.com/tmdeveloper007/arnio/issues/422)
* apply black formatting and remove trailing blank line ([f5db04f](https://github.com/tmdeveloper007/arnio/commit/f5db04fa1388bd6dc339be732aa1411b613e8fcf))
* **bindings:** prevent dangling pointer in to_numpy_float/int ([#28](https://github.com/tmdeveloper007/arnio/issues/28)) ([#805](https://github.com/tmdeveloper007/arnio/issues/805)) ([f28a207](https://github.com/tmdeveloper007/arnio/commit/f28a207a9e897a86f242ffd6e42edcd9d73c8669))
* **cleaning:** accept sequence subsets in parse_bool_strings ([#766](https://github.com/tmdeveloper007/arnio/issues/766)) ([c1c25d6](https://github.com/tmdeveloper007/arnio/commit/c1c25d619bbccabb9e7df679d607f7075150f686))
* **cleaning:** preserve filter_rows column context on invalid comparisons ([ce10c2f](https://github.com/tmdeveloper007/arnio/commit/ce10c2f1633c6fecec52a53431783761b4eedc70))
* **cleaning:** preserve Unicode bytes in normalize_case ([ca6afe6](https://github.com/tmdeveloper007/arnio/commit/ca6afe63397b619ac3f8326ec82bdab31bd9475c)), closes [#26](https://github.com/tmdeveloper007/arnio/issues/26)
* **cleaning:** reject lossy and non-finite fill_nulls values ([cbd7d81](https://github.com/tmdeveloper007/arnio/commit/cbd7d81f5bdee6c47385fb46a3ab480a2bcae0ef))
* **cleaning:** validate parse_bool_strings custom tokens ([1036f0b](https://github.com/tmdeveloper007/arnio/commit/1036f0b0d548af69e947219438208cf54b5a7f8b))
* clear errors for unsupported pandas dtypes in from_pandas() ([626a13c](https://github.com/tmdeveloper007/arnio/commit/626a13c8fb3416ff3e077bfec2f333b94309a29b)), closes [#460](https://github.com/tmdeveloper007/arnio/issues/460)
* coerce types in Column::push_back ([525ae75](https://github.com/tmdeveloper007/arnio/commit/525ae75ca88687f5dfb74967ea5512588c3ac06c))
* coerce types in Column::push_back ([ae4d9a0](https://github.com/tmdeveloper007/arnio/commit/ae4d9a0f2d12e9137d381dc0ebdc00dc458d1868))
* correct indentation in test_from_pandas_unsupported_scalar_object_column ([f97bb25](https://github.com/tmdeveloper007/arnio/commit/f97bb253ce4caa41bd5f41a15eda170c6018091a))
* **csv_writer:** open output file in binary mode ([#752](https://github.com/tmdeveloper007/arnio/issues/752)) ([088c81f](https://github.com/tmdeveloper007/arnio/commit/088c81f12c949be14dfb345c3070bc90cc2a51ad)), closes [#717](https://github.com/tmdeveloper007/arnio/issues/717)
* **csv:** normalize trailing empty fields ([62314d7](https://github.com/tmdeveloper007/arnio/commit/62314d741c5958b2ffbbd94e9ea362f8909520af)), closes [#116](https://github.com/tmdeveloper007/arnio/issues/116)
* **csv:** preserve leading-zero identifier inference ([8aa3f15](https://github.com/tmdeveloper007/arnio/commit/8aa3f15df9724a0c37d6ca2e9578352f012aea21))
* **csv:** reject late NUL bytes in UTF-8 input ([0152a68](https://github.com/tmdeveloper007/arnio/commit/0152a68510f541efaf845165d4ec53fd34e021e4))
* escape markdown pipes in quality report ([#781](https://github.com/tmdeveloper007/arnio/issues/781)) ([8ca3074](https://github.com/tmdeveloper007/arnio/commit/8ca30749a3ab5122a052cd99651b1515d4ffe34d))
* explicitly reject keep=True in drop_duplicates ([#584](https://github.com/tmdeveloper007/arnio/issues/584)) ([#787](https://github.com/tmdeveloper007/arnio/issues/787)) ([1d4993a](https://github.com/tmdeveloper007/arnio/commit/1d4993a99eb55e833a9dd22c59fe5d5b3c8fb188))
* handle empty CSV files with a dedicated error path ([b359173](https://github.com/tmdeveloper007/arnio/commit/b359173f15b5cf6b4cb68b9f04b418d5380c0c44))
* improve nested object error messages in from_pandas ([ca90974](https://github.com/tmdeveloper007/arnio/commit/ca90974cdef4b25824525aa2d4482968054adba2))
* keep decimal-looking strings on float path ([#788](https://github.com/tmdeveloper007/arnio/issues/788)) ([d8cea07](https://github.com/tmdeveloper007/arnio/commit/d8cea0728d938837e1a355cf56f74d82efeffa09))
* make custom pipeline step registry thread-safe ([2755772](https://github.com/tmdeveloper007/arnio/commit/27557721616a078d4302f9cc7aa2e9f2750b96f5))
* make suggested cleaning kwargs deterministic in to_markdown ([#771](https://github.com/tmdeveloper007/arnio/issues/771)) ([5a280d2](https://github.com/tmdeveloper007/arnio/commit/5a280d28c5247abb9d5bb34062110c358b422758))
* move test_pipeline_clip_numeric inside TestPipeline class ([8ca3bb2](https://github.com/tmdeveloper007/arnio/commit/8ca3bb22afdec2b22056bb64a6324f098324847b))
* normalize title case across punctuation boundaries ([4a9b947](https://github.com/tmdeveloper007/arnio/commit/4a9b947f4045edf61839e70247fcce5b54fe5b1d))
* **pandas:** reject stringified column label collisions ([c3e1d3d](https://github.com/tmdeveloper007/arnio/commit/c3e1d3d006b0cefd6eefdff38659e94dcc05b7b5)), closes [#711](https://github.com/tmdeveloper007/arnio/issues/711)
* **pipeline:** raise TypeError for custom steps returning non-DataFra… ([#687](https://github.com/tmdeveloper007/arnio/issues/687)) ([0008c21](https://github.com/tmdeveloper007/arnio/commit/0008c21bed342e87d2d27e8f2b960716b62542ee))
* **pipeline:** reject custom steps that shadow built-ins ([b3bf090](https://github.com/tmdeveloper007/arnio/commit/b3bf0901a6c81999df7bb2e28e88e6ba460410ec))
* preserve 1-based source row numbers in schema validation issues ([5f538fd](https://github.com/tmdeveloper007/arnio/commit/5f538fd2b508b4c791967c8f9b1947387c6467c2))
* preserve 1-based source row numbers in schema validation issues ([3ea089a](https://github.com/tmdeveloper007/arnio/commit/3ea089af93c149c179bbd183c1efde5ff3ebf3cf)), closes [#213](https://github.com/tmdeveloper007/arnio/issues/213)
* preserve column order in scan_csv schema ([a3864f0](https://github.com/tmdeveloper007/arnio/commit/a3864f0640580acdf979d71c18c25ce8c6a9456d))
* preserve Int64 dtype for all-null nullable integer columns in from_pandas roundtrip ([#394](https://github.com/tmdeveloper007/arnio/issues/394)) ([ef726ed](https://github.com/tmdeveloper007/arnio/commit/ef726ed0e1af588c7c0f74a04e02ccfd6a1d688f))
* preserve non-utf8 scan samples ([da5bf15](https://github.com/tmdeveloper007/arnio/commit/da5bf15f4ca9add2530e763acb65902c61956f11)), closes [#579](https://github.com/tmdeveloper007/arnio/issues/579)
* preserve null-valued replace_values results ([#800](https://github.com/tmdeveloper007/arnio/issues/800)) ([5aaf070](https://github.com/tmdeveloper007/arnio/commit/5aaf070483e988d3acc7e9effcbb92b6199cf2f8))
* preserve quoted CSV line endings ([8324322](https://github.com/tmdeveloper007/arnio/commit/8324322d2f32dea78a70dc5fea55e4ccccb4e5f2))
* **quality:** correct compare_profiles drift thresholds ([#750](https://github.com/tmdeveloper007/arnio/issues/750)) ([f7b72a3](https://github.com/tmdeveloper007/arnio/commit/f7b72a3e49c65f3cd49c7014db31211382bdb263))
* raise TypeError for nested data in from_pandas ([7389289](https://github.com/tmdeveloper007/arnio/commit/73892893df44f38fa3f0600c26e92965eb029b4a))
* raise TypeError for nested data in from_pandas ([31118b6](https://github.com/tmdeveloper007/arnio/commit/31118b62e39b460381f75644cc23134199a8e950))
* reject duplicate pandas column labels ([5316cf8](https://github.com/tmdeveloper007/arnio/commit/5316cf8b3da3c6d552ffc5910748dad29f69cda0))
* reject empty write_csv line terminators ([#757](https://github.com/tmdeveloper007/arnio/issues/757)) ([859d4b9](https://github.com/tmdeveloper007/arnio/commit/859d4b998f4428fdf4ef0a3dacec2899c9aa6485))
* reject impossible schema bounds ([906b286](https://github.com/tmdeveloper007/arnio/commit/906b286ad0bae551bea56746f90fa95135f749ab))
* reject late nul bytes in csv inputs ([#760](https://github.com/tmdeveloper007/arnio/issues/760)) ([f140aaf](https://github.com/tmdeveloper007/arnio/commit/f140aaf31a451c278b408a6f99259288f2e43336))
* reject newline delimiters in write_csv ([#755](https://github.com/tmdeveloper007/arnio/issues/755)) ([58a265f](https://github.com/tmdeveloper007/arnio/commit/58a265ff30e86f7f893fa8385adb871bd7a65f3c))
* reject quote delimiter in write_csv ([#756](https://github.com/tmdeveloper007/arnio/issues/756)) ([3f8c68f](https://github.com/tmdeveloper007/arnio/commit/3f8c68fdca49c95a60110cf43f2345deb53601ed))
* reject unsupported object scalars ([75af857](https://github.com/tmdeveloper007/arnio/commit/75af85757e9680ae48ea231863199b723e8f3ad9))
* remove unused import in setup.py ([6590c85](https://github.com/tmdeveloper007/arnio/commit/6590c85d3527fd260566120aaba84eb245e6af78))
* remove unused import in setup.py ([92d3246](https://github.com/tmdeveloper007/arnio/commit/92d32466f7c4a2643827ec38bda616876b4e08a7))
* reorder bool and int type checks in fill_nulls binding ([b8bbebe](https://github.com/tmdeveloper007/arnio/commit/b8bbebe8012f086cb986bf1cdbad5bfdd35ac4f5))
* reorder bool and int type checks in fill_nulls binding ([e3c0907](https://github.com/tmdeveloper007/arnio/commit/e3c0907544f59e8bcee53fbc296576e8bffaccba))
* resolve CountryCode validator allowlist and uniqueness ([eb7b34f](https://github.com/tmdeveloper007/arnio/commit/eb7b34fcb75b78d5e6803e1c0d19d734f47a3ca3)), closes [#714](https://github.com/tmdeveloper007/arnio/issues/714)
* respect non-utf8 scan sample count ([#761](https://github.com/tmdeveloper007/arnio/issues/761)) ([4cd43c5](https://github.com/tmdeveloper007/arnio/commit/4cd43c5befc5bddd28ce896e6a6254f634af8f12))
* restore missing imports and fix test failures ([1e700a7](https://github.com/tmdeveloper007/arnio/commit/1e700a78367cff96f4f7bb72736b27f91b8afe73))
* revert unrelated README changes and add non-string type validation ([d5937bf](https://github.com/tmdeveloper007/arnio/commit/d5937bf869840dc440d7e74e8d1de14711f370cb))
* **schema:** add redaction support to markdown validation reports ([e523129](https://github.com/tmdeveloper007/arnio/commit/e5231293b2825c47ed7f09d88b3d9287458a7513)), closes [#682](https://github.com/tmdeveloper007/arnio/issues/682)
* **schema:** reject invalid unique configuration in validate ([a960498](https://github.com/tmdeveloper007/arnio/commit/a9604986aaf5330a84ba2344ddd54bf5afbbb4cf))
* skip numeric cast suggestions for identifier-like columns ([cf687e2](https://github.com/tmdeveloper007/arnio/commit/cf687e2ae83b4cc1c1edef6065920a12fbc7a7ad))
* skip numeric cast suggestions for identifier-like columns ([928398f](https://github.com/tmdeveloper007/arnio/commit/928398fa4eda7fed0f2424e58f442d7781483234))
* strip whitespace from CSV headers ([675452f](https://github.com/tmdeveloper007/arnio/commit/675452f4317e277c25d625efead49bb1682637fa))
* sync version in __init__.py with pyproject.toml ([b159520](https://github.com/tmdeveloper007/arnio/commit/b159520e250e07759b46068df8f9cf52bf7a2851))
* sync version in __init__.py with pyproject.toml ([c3eb21e](https://github.com/tmdeveloper007/arnio/commit/c3eb21e166147dc8069bb699a5cc4c8db4925188))
* use one-based composite unique row indexes ([#782](https://github.com/tmdeveloper007/arnio/issues/782)) ([cdd1368](https://github.com/tmdeveloper007/arnio/commit/cdd1368ea9520360965cdcb99337df913f421b51))
* use relative import for _arnio_cpp ([fc0c3d6](https://github.com/tmdeveloper007/arnio/commit/fc0c3d6b0e12bbb1f74dc3ba6ada29b551bcf6da))
* use relative import for _arnio_cpp ([adb45aa](https://github.com/tmdeveloper007/arnio/commit/adb45aa3f85069afee5d1778ff1010350dae0e35))
* use typing.Callable instead of callable in pipeline.py type hint ([5d64cb1](https://github.com/tmdeveloper007/arnio/commit/5d64cb1ded77700b72b7f7c6725bf92fd0e9491c))
* use typing.Callable instead of callable in pipeline.py type hint ([661b344](https://github.com/tmdeveloper007/arnio/commit/661b3447c2fe4593ecfee23294d27ace90ce18c0))
* validate drop_duplicates keep option ([#758](https://github.com/tmdeveloper007/arnio/issues/758)) ([a12a5b1](https://github.com/tmdeveloper007/arnio/commit/a12a5b1dba68d5c30064c0f41dff954df923b5c6))
* validate file extension and content in read_csv ([7d7582c](https://github.com/tmdeveloper007/arnio/commit/7d7582ca0ff14d4062ce6951a96a09ba27c43a6c))
* validate file extension and content in read_csv ([058b0ee](https://github.com/tmdeveloper007/arnio/commit/058b0ee1a9f83b597c7bd74cafd0a7a06d673c1c))
* validate missing columns in filter_rows ([e0514ef](https://github.com/tmdeveloper007/arnio/commit/e0514ef04fea19fb07fd7373539e1a5019e2763b))
* validate pipeline steps before execution ([#693](https://github.com/tmdeveloper007/arnio/issues/693)) ([d102429](https://github.com/tmdeveloper007/arnio/commit/d102429eced6a92c83cb3d6d1728bf810ea9ba7d))
* validate schema field values early ([#748](https://github.com/tmdeveloper007/arnio/issues/748)) ([bf9d6ba](https://github.com/tmdeveloper007/arnio/commit/bf9d6bab605235841f60f61179838adca0e8d949))
* validate Schema.unique string and invalid unique members ([#776](https://github.com/tmdeveloper007/arnio/issues/776)) ([866ffc5](https://github.com/tmdeveloper007/arnio/commit/866ffc59240542300dae27a97fcda878c9abaea6))
* validate UInt64 conversion bounds ([32ae8a4](https://github.com/tmdeveloper007/arnio/commit/32ae8a43d2858c14d32122d236767d5d1453a837)), closes [#626](https://github.com/tmdeveloper007/arnio/issues/626)
* validate write_csv delimiter type ([#759](https://github.com/tmdeveloper007/arnio/issues/759)) ([ca69adf](https://github.com/tmdeveloper007/arnio/commit/ca69adf1980c07d7866e64ad11f1255b0d98b384))


### Performance Improvements

* add approximate top-values profiling ([#762](https://github.com/tmdeveloper007/arnio/issues/762)) ([0d1168b](https://github.com/tmdeveloper007/arnio/commit/0d1168b0d294310f0772496b6f1290d6e9e8ac0c))
* add auto-clean memory benchmark ([8bd10f4](https://github.com/tmdeveloper007/arnio/commit/8bd10f4c7301d210a0dcebb64d27006274308705))
* add measurement script for to_pandas conversion overhead ([#556](https://github.com/tmdeveloper007/arnio/issues/556)) ([6c15c53](https://github.com/tmdeveloper007/arnio/commit/6c15c5337ea09cdbe552733e871e09adca704895))
* add process RSS metrics to benchmark ([6206cbd](https://github.com/tmdeveloper007/arnio/commit/6206cbda592705d20877d8a89e2f899025f2f329))
* **cleaning:** add native safe_divide_columns numeric path ([7179a95](https://github.com/tmdeveloper007/arnio/commit/7179a953472f39892ac4063d1cedd6e6c35d739f))
* **cleaning:** implement native clip_numeric without pandas round-trip ([eed031f](https://github.com/tmdeveloper007/arnio/commit/eed031f02c01f48db21f6a7c005dc310cc7d205c)), closes [#657](https://github.com/tmdeveloper007/arnio/issues/657)
* native normalize_unicode without pandas roundtrip ([38a6860](https://github.com/tmdeveloper007/arnio/commit/38a6860638f79035973899d6023829fef5c76624))
* release GIL around long C++ operations ([1100fec](https://github.com/tmdeveloper007/arnio/commit/1100fec21ad05a6288a945af1e88754b7a787280))
* stream transcode and sample rows for scan_csv schema inference ([713aeaa](https://github.com/tmdeveloper007/arnio/commit/713aeaa9ccb380bb68568999edc141e1dc73389b))


### Documentation

* add API reference skeleton ([5ea384d](https://github.com/tmdeveloper007/arnio/commit/5ea384d9341aab15fdbe053ff0388d8f1430cf48))
* add architecture guide, reframe benchmarks, add social preview ([f91e69e](https://github.com/tmdeveloper007/arnio/commit/f91e69e7ffb89adcaa4ed64a5ddd4173e889c045))
* add architecture guide, reframe benchmarks, add social preview ([ab2ddba](https://github.com/tmdeveloper007/arnio/commit/ab2ddbaf422b582b5fc855df71906612936568e9))
* add beginner-friendly auto_clean tutorial with profiling and cleaning workflow  ([#326](https://github.com/tmdeveloper007/arnio/issues/326)) ([b604a0d](https://github.com/tmdeveloper007/arnio/commit/b604a0d067f6603cf6bb5037b5b33b6ff0c19248))
* add CLI roadmap and command examples ([1f4f61d](https://github.com/tmdeveloper007/arnio/commit/1f4f61d5a1c013179ec914931a713a5a833310e5)), closes [#671](https://github.com/tmdeveloper007/arnio/issues/671)
* add comprehensive docstrings to all public Python functions ([3cbe1b3](https://github.com/tmdeveloper007/arnio/commit/3cbe1b35b95678ecc7aa267663dcd998dd74d0f2))
* add contributor glossary ([#308](https://github.com/tmdeveloper007/arnio/issues/308)) ([da52804](https://github.com/tmdeveloper007/arnio/commit/da5280486603e2d630adf33ec8d7162acb9ba0ba))
* add contributors section to README ([70ba51a](https://github.com/tmdeveloper007/arnio/commit/70ba51a6af1922370a0bda70c79ac5ab620f32d3))
* add CSV error handling guidance ([10aa0b7](https://github.com/tmdeveloper007/arnio/commit/10aa0b70f18026671ac9baeb94443fa27b2d46aa)), closes [#490](https://github.com/tmdeveloper007/arnio/issues/490)
* add data contract CI workflow example ([ab83194](https://github.com/tmdeveloper007/arnio/commit/ab83194e81e667997cce23d30663d1efac33616f))
* add data quality report examples [#279](https://github.com/tmdeveloper007/arnio/issues/279) ([#295](https://github.com/tmdeveloper007/arnio/issues/295)) ([ca42e87](https://github.com/tmdeveloper007/arnio/commit/ca42e87cf2c596b78286ab3fe4ce8a9c305a6f2a))
* add Discord community links ([#305](https://github.com/tmdeveloper007/arnio/issues/305)) ([64cb4a1](https://github.com/tmdeveloper007/arnio/commit/64cb4a1d871ac7ec8471e28c5386eb8ebfb20ef4))
* add financial CSV cleaning example notebook ([e9fb6f6](https://github.com/tmdeveloper007/arnio/commit/e9fb6f6f793538354160584effd87bf866f85eee))
* add Google Colab install smoke test guide ([99803df](https://github.com/tmdeveloper007/arnio/commit/99803dff307e6934c8d86cf138234bc98caecaa6))
* add gssoc faq ([#309](https://github.com/tmdeveloper007/arnio/issues/309)) ([dc32e56](https://github.com/tmdeveloper007/arnio/commit/dc32e563ba5ff8e2ed2680dec9451d27c65a14e5))
* add interoperability examples ([aa7c7d7](https://github.com/tmdeveloper007/arnio/commit/aa7c7d77d1dcca8a6b7f416ef358a4c6f7ac8edc))
* add issue triage guide for maintainers ([#300](https://github.com/tmdeveloper007/arnio/issues/300)) ([2d6dd6f](https://github.com/tmdeveloper007/arnio/commit/2d6dd6f9c566479757c2146f02e186c1d7d57c2e))
* add JSONL pipeline processing example ([8db4886](https://github.com/tmdeveloper007/arnio/commit/8db48867e90591fbd2ff0f7be1764c6165ab77a5)), closes [#864](https://github.com/tmdeveloper007/arnio/issues/864)
* add language identifiers to unlabeled fenced code blocks (MD040) ([21aad9c](https://github.com/tmdeveloper007/arnio/commit/21aad9c06e1440efa20d377f7842da6afa8d9095))
* add pipeline backend execution map ([#744](https://github.com/tmdeveloper007/arnio/issues/744)) ([e4f368e](https://github.com/tmdeveloper007/arnio/commit/e4f368ecd343e5d513a5c1d71a55b7e98d3925ce))
* add quality and schema architecture flow ([d22fa56](https://github.com/tmdeveloper007/arnio/commit/d22fa56c393c2005c9a351f30ca6132c4ae3c863))
* add quick example section to README ([#794](https://github.com/tmdeveloper007/arnio/issues/794)) ([c9a59a2](https://github.com/tmdeveloper007/arnio/commit/c9a59a2b2cf4b94033538f1242598db4942fe84b))
* add release process guide ([#304](https://github.com/tmdeveloper007/arnio/issues/304)) ([f5e1325](https://github.com/tmdeveloper007/arnio/commit/f5e13252889865e24cd464379c9fa3974d2fff03))
* add troubleshooting guide ([#791](https://github.com/tmdeveloper007/arnio/issues/791)) ([7f3d607](https://github.com/tmdeveloper007/arnio/commit/7f3d60701db10db1471670308c3642004bfd72ca))
* align pandas dtype support documentation with implementation ([#327](https://github.com/tmdeveloper007/arnio/issues/327)) ([badd815](https://github.com/tmdeveloper007/arnio/commit/badd8150a3859ffb1598bdf21f71a8cd2c4c6b0b))
* catalog resolved Issue [#644](https://github.com/tmdeveloper007/arnio/issues/644) in issues_list.md ([1e6b592](https://github.com/tmdeveloper007/arnio/commit/1e6b5924fcb8f6a2cc97a59f789816ba7273885a))
* catalog resolved Issue [#680](https://github.com/tmdeveloper007/arnio/issues/680) in issues_list.md ([637c8b1](https://github.com/tmdeveloper007/arnio/commit/637c8b11820eee283693d6652266e51c28c453c6))
* completely overhaul and beautify README.md ([aef6497](https://github.com/tmdeveloper007/arnio/commit/aef649771e83668d3a47cd11b41b2c230950cd96))
* completely redesign README with flagship-quality presentation ([252988a](https://github.com/tmdeveloper007/arnio/commit/252988a770a0600074734ed44b48e7cbd6763a66))
* completely redesign README with flagship-quality presentation ([5953eb4](https://github.com/tmdeveloper007/arnio/commit/5953eb4a567e9941a9a5ff3c4bc892a19605c737))
* document auto_clean strict mode risks ([#764](https://github.com/tmdeveloper007/arnio/issues/764)) ([12c6b36](https://github.com/tmdeveloper007/arnio/commit/12c6b36f340563cd4ab482b459fb3b0aa437e5e8))
* document newly resolved GSSoC pull requests ([d3be923](https://github.com/tmdeveloper007/arnio/commit/d3be92349203801643ccc12f6a22fe621e7a19b3))
* document pandas index conversion behavior ([#407](https://github.com/tmdeveloper007/arnio/issues/407)) ([327b650](https://github.com/tmdeveloper007/arnio/commit/327b650bb40b8ba902c5b0dc903b98d5f3e1172e))
* document sklearn row-dropping pipeline behavior ([#786](https://github.com/tmdeveloper007/arnio/issues/786)) ([371f886](https://github.com/tmdeveloper007/arnio/commit/371f886a1a74c3e86f28683331cae9daf3655413))
* document ValidationResult row-index convention (1-based, header excluded) ([#803](https://github.com/tmdeveloper007/arnio/issues/803)) ([a4f3965](https://github.com/tmdeveloper007/arnio/commit/a4f3965cc9d74cc2f62d6ab4bba81136ffb62c3b))
* document write_csv validation behavior ([4588666](https://github.com/tmdeveloper007/arnio/commit/45886660c5087d80ab2aeb39ebd64562836805e8)), closes [#664](https://github.com/tmdeveloper007/arnio/issues/664)
* duplicated code ([62401a1](https://github.com/tmdeveloper007/arnio/commit/62401a1418acb149b74697495467fd05e22fa14f))
* enforce conventional commits in contributor guidelines ([d98f6cf](https://github.com/tmdeveloper007/arnio/commit/d98f6cf208f8acc5d34dc0bee280f28a64cc1dbe))
* expand pipeline execution and cleaning module architecture ([17e51af](https://github.com/tmdeveloper007/arnio/commit/17e51af852fa0c3c306b9d1581752eddafc0fe4b))
* filter unassigned issues by needs maintainer/needs triage labels ([ce9031f](https://github.com/tmdeveloper007/arnio/commit/ce9031f767ebb38299ba21457b66620e8b6c857b))
* fix non-sequential roadmap versions ([#107](https://github.com/tmdeveloper007/arnio/issues/107)) ([db3b8e4](https://github.com/tmdeveloper007/arnio/commit/db3b8e47fc721ad899df0b6239bc706824d168a5))
* implement Phase 2 contributor infrastructure and issue templates ([ae8d377](https://github.com/tmdeveloper007/arnio/commit/ae8d377b6bacf8623ff0d1a185c27217f6623d14))
* improve quickstart wording ([a3f37d9](https://github.com/tmdeveloper007/arnio/commit/a3f37d94146f5f1b3939b0962236242312dadcac))
* include pandas dtype fix in 1.11.2 notes ([2385b3a](https://github.com/tmdeveloper007/arnio/commit/2385b3acb3fe92b11c266cd2321ad2d662a76472))
* premium landing page overhaul for README ([693e5e4](https://github.com/tmdeveloper007/arnio/commit/693e5e4be6d67cf45e903e4a2dcd111bacb48959))
* prepare repository for GSSoC contributors ([#289](https://github.com/tmdeveloper007/arnio/issues/289)) ([d270812](https://github.com/tmdeveloper007/arnio/commit/d2708126a20d6e12be75a438d631f84aa802e13f))
* remove duplicated code ([0e215f9](https://github.com/tmdeveloper007/arnio/commit/0e215f9080abbe77183f51a9a1b07e90d60bc54f))
* remove large Discord badge from README ([#307](https://github.com/tmdeveloper007/arnio/issues/307)) ([1f0ff3a](https://github.com/tmdeveloper007/arnio/commit/1f0ff3ab15d111344cc9c6281226ef6361f919f9))
* replace ASCII architecture diagram with Mermaid flowchart ([abede39](https://github.com/tmdeveloper007/arnio/commit/abede392dfd11ac909d273c90cfc01463522004b))
* rewrite README with differentiation, performance benchmarks, and intro gif ([14b9820](https://github.com/tmdeveloper007/arnio/commit/14b982055e14854f0542e998e5da039b50c7b6f9))
* standardize Google-style docstrings in arnio/schema.py ([dc5aa3d](https://github.com/tmdeveloper007/arnio/commit/dc5aa3d9036651c1190884ca376f1f0090796f98))


### Miscellaneous Chores

* **main:** release 1.10.0 ([2bb83b2](https://github.com/tmdeveloper007/arnio/commit/2bb83b20d766a64ff219c067ed1828fbf582e99d))
* **main:** release 1.9.1 ([ab6a2d6](https://github.com/tmdeveloper007/arnio/commit/ab6a2d67a1ecfddd37ffef9488aa7dbdafc40af6))

## [1.14.0](https://github.com/im-anishraj/arnio/compare/v1.13.0...v1.14.0) (2026-05-18)


### Features

* add parse_bool_strings pipeline step ([bc6e53d](https://github.com/im-anishraj/arnio/commit/bc6e53d6cbf73c02bcbd81f828a6c085ed928797)), closes [#150](https://github.com/im-anishraj/arnio/issues/150)


### Documentation

* add interoperability examples ([aa7c7d7](https://github.com/im-anishraj/arnio/commit/aa7c7d77d1dcca8a6b7f416ef358a4c6f7ac8edc))

## [1.13.0](https://github.com/im-anishraj/arnio/compare/v1.12.1...v1.13.0) (2026-05-18)


### Features

* add benchmark regression reporting ([#554](https://github.com/im-anishraj/arnio/issues/554)) ([83b9ee5](https://github.com/im-anishraj/arnio/commit/83b9ee5c8cf75477ebb476f1fb3f13654eceab3a))
* add quality sample redaction ([#555](https://github.com/im-anishraj/arnio/issues/555)) ([daece46](https://github.com/im-anishraj/arnio/commit/daece46037eab5bc924d8e61b4111dc659301ed9))
* add Regex field validator to schema ([#537](https://github.com/im-anishraj/arnio/issues/537)) ([70b1839](https://github.com/im-anishraj/arnio/commit/70b18395066c424e143a1a8eb034f3f200d92333))
* add string length statistics to quality profile (resolves [#174](https://github.com/im-anishraj/arnio/issues/174)) ([#550](https://github.com/im-anishraj/arnio/issues/550)) ([98d1bf3](https://github.com/im-anishraj/arnio/commit/98d1bf34a9b175610efbb360d034ce0663a8a547))

## [1.12.1](https://github.com/im-anishraj/arnio/compare/v1.12.0...v1.12.1) (2026-05-18)


### Bug Fixes

* make custom pipeline step registry thread-safe ([2755772](https://github.com/im-anishraj/arnio/commit/27557721616a078d4302f9cc7aa2e9f2750b96f5))


### Performance Improvements

* release GIL around long C++ operations ([1100fec](https://github.com/im-anishraj/arnio/commit/1100fec21ad05a6288a945af1e88754b7a787280))

## [1.12.0](https://github.com/im-anishraj/arnio/compare/v1.11.3...v1.12.0) (2026-05-17)


### Features

* add strip_whitespace allocation benchmark ([e2ff584](https://github.com/im-anishraj/arnio/commit/e2ff58416125fe1eae4bef4c204cc52fb248fb86))


### Documentation

* replace ASCII architecture diagram with Mermaid flowchart ([abede39](https://github.com/im-anishraj/arnio/commit/abede392dfd11ac909d273c90cfc01463522004b))

## [1.11.3](https://github.com/im-anishraj/arnio/compare/v1.11.2...v1.11.3) (2026-05-17)


### Documentation

* add API reference skeleton ([5ea384d](https://github.com/im-anishraj/arnio/commit/5ea384d9341aab15fdbe053ff0388d8f1430cf48))

## [1.11.2](https://github.com/im-anishraj/arnio/compare/v1.11.1...v1.11.2) (2026-05-17)


### Bug Fixes

* raise clear errors for unsupported pandas dtypes in from_pandas ([1791e4f](https://github.com/im-anishraj/arnio/commit/1791e4f05242841e7878fd8c03a185bb01c48ae1))
* preserve 1-based source row numbers in schema validation issues ([5f538fd](https://github.com/im-anishraj/arnio/commit/5f538fd2b508b4c791967c8f9b1947387c6467c2))

## [1.11.1](https://github.com/im-anishraj/arnio/compare/v1.11.0...v1.11.1) (2026-05-17)


### Bug Fixes

* skip numeric cast suggestions for identifier-like columns ([cf687e2](https://github.com/im-anishraj/arnio/commit/cf687e2ae83b4cc1c1edef6065920a12fbc7a7ad))

## [1.11.0](https://github.com/im-anishraj/arnio/compare/v1.10.0...v1.11.0) (2026-05-17)


### Features

* add scikit-learn ArnioCleaner transformer ([610a39f](https://github.com/im-anishraj/arnio/commit/610a39fe5ab4a02db2ad7f9c3223896cdf263db5))
* register combine_columns as pipeline step and add test ([beaf402](https://github.com/im-anishraj/arnio/commit/beaf4022ac7dc70cb370d387769fc033beb4454d))

## [1.10.0](https://github.com/im-anishraj/arnio/compare/v1.9.1...v1.10.0) (2026-05-17)


### Features

* add DateTime schema field ([05c26be](https://github.com/im-anishraj/arnio/commit/05c26bebf1cf79bbdbb98157dba1618c61abd08e))
* add normalize_unicode cleaning step ([c8c7c40](https://github.com/im-anishraj/arnio/commit/c8c7c40c9172e83d289b25e2e4b797efd78cd26a))
* add top_values summary for categorical columns ([f593f94](https://github.com/im-anishraj/arnio/commit/f593f94cf331180f29516d1afc217c106a96ad8b))


### Performance Improvements

* add process RSS metrics to benchmark ([6206cbd](https://github.com/im-anishraj/arnio/commit/6206cbda592705d20877d8a89e2f899025f2f329))


### Documentation

* add financial CSV cleaning example notebook ([e9fb6f6](https://github.com/im-anishraj/arnio/commit/e9fb6f6f793538354160584effd87bf866f85eee))

## [1.9.1](https://github.com/im-anishraj/arnio/compare/v1.9.0...v1.9.1) (2026-05-17)


### Performance Improvements

* stream transcode and sample rows for scan_csv schema inference ([713aeaa](https://github.com/im-anishraj/arnio/commit/713aeaa9ccb380bb68568999edc141e1dc73389b))

## [1.9.0](https://github.com/im-anishraj/arnio/compare/v1.8.0...v1.9.0) (2026-05-17)


### Features

* add composite uniqueness validation support ([#495](https://github.com/im-anishraj/arnio/issues/495)) ([8b11e19](https://github.com/im-anishraj/arnio/commit/8b11e19180b97fde1c380857e702d78dc7df8fc8))
* add CountryCode schema validator ([#487](https://github.com/im-anishraj/arnio/issues/487)) ([14a77e5](https://github.com/im-anishraj/arnio/commit/14a77e532409bffc0fdef85fbbbaaa798782dde7))
* add replace_values pipeline step ([#348](https://github.com/im-anishraj/arnio/issues/348)) ([02b297c](https://github.com/im-anishraj/arnio/commit/02b297c0d60fdb4417e801f2f28db92f50441a4c))


### Documentation

* document pandas index conversion behavior ([#407](https://github.com/im-anishraj/arnio/issues/407)) ([327b650](https://github.com/im-anishraj/arnio/commit/327b650bb40b8ba902c5b0dc903b98d5f3e1172e))

## [1.8.0](https://github.com/im-anishraj/arnio/compare/v1.7.0...v1.8.0) (2026-05-17)


### Features

* add ArFrame.select_dtypes for type-based column selection ([7899541](https://github.com/im-anishraj/arnio/commit/7899541113aad0f300decc08b94f285b920f3008))
* add trim_column_names cleaning primitive and pipeline step ([d064335](https://github.com/im-anishraj/arnio/commit/d0643355f1f626a4ee2a4264aea67e316971df76))


### Bug Fixes

* reject impossible schema bounds ([906b286](https://github.com/im-anishraj/arnio/commit/906b286ad0bae551bea56746f90fa95135f749ab))

## [1.7.0](https://github.com/im-anishraj/arnio/compare/v1.6.2...v1.7.0) (2026-05-17)


### Features

* add keep_rows_with_nulls pipeline step ([37dde00](https://github.com/im-anishraj/arnio/commit/37dde009d3899e3647183f34209f171afca11f31))


### Bug Fixes

* add YAML validation for GitHub workflow files ([0c666ca](https://github.com/im-anishraj/arnio/commit/0c666caa0ce937d70fdffc58dee2e8ba12338412))


### Performance Improvements

* add auto-clean memory benchmark ([8bd10f4](https://github.com/im-anishraj/arnio/commit/8bd10f4c7301d210a0dcebb64d27006274308705))

## [1.6.2](https://github.com/im-anishraj/arnio/compare/v1.6.1...v1.6.2) (2026-05-17)


### Documentation

* improve quickstart wording ([a3f37d9](https://github.com/im-anishraj/arnio/commit/a3f37d94146f5f1b3939b0962236242312dadcac))

## [1.6.1](https://github.com/im-anishraj/arnio/compare/v1.6.0...v1.6.1) (2026-05-16)


### Bug Fixes

* preserve column order in scan_csv schema ([a3864f0](https://github.com/im-anishraj/arnio/commit/a3864f0640580acdf979d71c18c25ce8c6a9456d))
* validate missing columns in filter_rows ([e0514ef](https://github.com/im-anishraj/arnio/commit/e0514ef04fea19fb07fd7373539e1a5019e2763b))

## [1.6.0](https://github.com/im-anishraj/arnio/compare/v1.5.1...v1.6.0) (2026-05-16)


### Features

* add to_pandas copy option ([1746fe1](https://github.com/im-anishraj/arnio/commit/1746fe15d5c399d649fff9561a7a02bea147c4de))

## [1.5.1](https://github.com/im-anishraj/arnio/compare/v1.5.0...v1.5.1) (2026-05-16)


### Bug Fixes

* normalize title case across punctuation boundaries ([4a9b947](https://github.com/im-anishraj/arnio/commit/4a9b947f4045edf61839e70247fcce5b54fe5b1d))

## [1.5.0](https://github.com/im-anishraj/arnio/compare/v1.4.0...v1.5.0) (2026-05-16)


### Features

* add is_empty convenience property to ArFrame ([37df94d](https://github.com/im-anishraj/arnio/commit/37df94d0e4f782fc4510ea8ad179960f51c0fc7d))
* add validation summary counts ([#444](https://github.com/im-anishraj/arnio/issues/444)) ([6575491](https://github.com/im-anishraj/arnio/commit/657549174aaca524ce77f169a7e7b3a7b230cba0))


### Bug Fixes

* allow encoded csv nul handling ([5796a35](https://github.com/im-anishraj/arnio/commit/5796a35a32aff5a5d889a72deee255232c527929)), closes [#422](https://github.com/im-anishraj/arnio/issues/422)

## [1.4.0](https://github.com/im-anishraj/arnio/compare/v1.3.1...v1.4.0) (2026-05-16)


### Features

* add bounded profiling sample_size validation ([1e31269](https://github.com/im-anishraj/arnio/commit/1e3126986bdc21e128fc734a71a77aa7f242441a))

## [1.3.1](https://github.com/im-anishraj/arnio/compare/v1.3.0...v1.3.1) (2026-05-16)


### Bug Fixes

* handle empty CSV files with a dedicated error path ([b359173](https://github.com/im-anishraj/arnio/commit/b359173f15b5cf6b4cb68b9f04b418d5380c0c44))

## [1.3.0](https://github.com/im-anishraj/arnio/compare/v1.2.0...v1.3.0) (2026-05-15)


### Features

* add column existence validation helper ([517d1e0](https://github.com/im-anishraj/arnio/commit/517d1e07d3b19252027ecdfac23d17b19e0aa793))
* add pandas integration direction ([#399](https://github.com/im-anishraj/arnio/issues/399)) ([22f9b58](https://github.com/im-anishraj/arnio/commit/22f9b58458383549d97d81ff7828b7a047063525))
* **convert:** preserve DataFrame attrs roundtrip ([4018f27](https://github.com/im-anishraj/arnio/commit/4018f27f76dbb021591b4aa6844e2c130887dceb))


### Bug Fixes

* preserve Int64 dtype for all-null nullable integer columns in from_pandas roundtrip ([#394](https://github.com/im-anishraj/arnio/issues/394)) ([ef726ed](https://github.com/im-anishraj/arnio/commit/ef726ed0e1af588c7c0f74a04e02ccfd6a1d688f))


### Documentation

* add quality and schema architecture flow ([d22fa56](https://github.com/im-anishraj/arnio/commit/d22fa56c393c2005c9a351f30ca6132c4ae3c863))

## [1.2.0](https://github.com/im-anishraj/arnio/compare/v1.1.1...v1.2.0) (2026-05-15)


### Features

* add ArFrame preview method ([814102e](https://github.com/im-anishraj/arnio/commit/814102e35b153cf75b3a759a5e33867edfe03321))
* add ArFrame select_columns helper ([fff406d](https://github.com/im-anishraj/arnio/commit/fff406d9a10943cb6f2bd76d32240933da90ed51))
* add clip_numeric cleaning helper ([4022449](https://github.com/im-anishraj/arnio/commit/4022449c7bbe5e31c94e756ff29a36b4c274a232))
* add drop constant columns ([#357](https://github.com/im-anishraj/arnio/issues/357)) ([3e13d3d](https://github.com/im-anishraj/arnio/commit/3e13d3d576add9fd8113cdf185ca08e61e75c4ee))
* add filter_rows pipeline step ([#288](https://github.com/im-anishraj/arnio/issues/288)) ([a3b7386](https://github.com/im-anishraj/arnio/commit/a3b7386e75bc45c9a7fde403ea373334ef528f75))
* add refactor task issue template ([#334](https://github.com/im-anishraj/arnio/issues/334)) ([6690947](https://github.com/im-anishraj/arnio/commit/6690947bcada6dc825853036a11ad2310acdd4e4))
* add round_numeric_columns cleaning helper ([61cd110](https://github.com/im-anishraj/arnio/commit/61cd1105e60c6daa38d34ef602f3f9fac28de7ea))
* add safe_divide_columns cleaning step ([80e4a65](https://github.com/im-anishraj/arnio/commit/80e4a654d81a1bd95e96b1f5ec83f5f82deff590))
* add trim_headers CSV option ([022460e](https://github.com/im-anishraj/arnio/commit/022460e1fa7e9510960a789aa38f835731dec700))
* add ValidationResult.to_markdown ([168e525](https://github.com/im-anishraj/arnio/commit/168e525409ce3a8d60f972dadacfaab01c4cafa8))
* enhance pull request template with media and performance sections ([#336](https://github.com/im-anishraj/arnio/issues/336)) ([99b588b](https://github.com/im-anishraj/arnio/commit/99b588b62910a68b83abdb39455c0d59de6bba56))


### Bug Fixes

* improve nested object error messages in from_pandas ([ca90974](https://github.com/im-anishraj/arnio/commit/ca90974cdef4b25824525aa2d4482968054adba2))


### Documentation

* add beginner-friendly auto_clean tutorial with profiling and cleaning workflow  ([#326](https://github.com/im-anishraj/arnio/issues/326)) ([b604a0d](https://github.com/im-anishraj/arnio/commit/b604a0d067f6603cf6bb5037b5b33b6ff0c19248))
* add contributor glossary ([#308](https://github.com/im-anishraj/arnio/issues/308)) ([da52804](https://github.com/im-anishraj/arnio/commit/da5280486603e2d630adf33ec8d7162acb9ba0ba))
* add data quality report examples [#279](https://github.com/im-anishraj/arnio/issues/279) ([#295](https://github.com/im-anishraj/arnio/issues/295)) ([ca42e87](https://github.com/im-anishraj/arnio/commit/ca42e87cf2c596b78286ab3fe4ce8a9c305a6f2a))
* add Discord community links ([#305](https://github.com/im-anishraj/arnio/issues/305)) ([64cb4a1](https://github.com/im-anishraj/arnio/commit/64cb4a1d871ac7ec8471e28c5386eb8ebfb20ef4))
* add gssoc faq ([#309](https://github.com/im-anishraj/arnio/issues/309)) ([dc32e56](https://github.com/im-anishraj/arnio/commit/dc32e563ba5ff8e2ed2680dec9451d27c65a14e5))
* add issue triage guide for maintainers ([#300](https://github.com/im-anishraj/arnio/issues/300)) ([2d6dd6f](https://github.com/im-anishraj/arnio/commit/2d6dd6f9c566479757c2146f02e186c1d7d57c2e))
* add release process guide ([#304](https://github.com/im-anishraj/arnio/issues/304)) ([f5e1325](https://github.com/im-anishraj/arnio/commit/f5e13252889865e24cd464379c9fa3974d2fff03))
* align pandas dtype support documentation with implementation ([#327](https://github.com/im-anishraj/arnio/issues/327)) ([badd815](https://github.com/im-anishraj/arnio/commit/badd8150a3859ffb1598bdf21f71a8cd2c4c6b0b))
* fix non-sequential roadmap versions ([#107](https://github.com/im-anishraj/arnio/issues/107)) ([db3b8e4](https://github.com/im-anishraj/arnio/commit/db3b8e47fc721ad899df0b6239bc706824d168a5))
* remove large Discord badge from README ([#307](https://github.com/im-anishraj/arnio/issues/307)) ([1f0ff3a](https://github.com/im-anishraj/arnio/commit/1f0ff3ab15d111344cc9c6281226ef6361f919f9))

## [1.1.1](https://github.com/im-anishraj/arnio/compare/v1.1.0...v1.1.1) (2026-05-14)


### Documentation

* prepare repository for GSSoC contributors ([#289](https://github.com/im-anishraj/arnio/issues/289)) ([d270812](https://github.com/im-anishraj/arnio/commit/d2708126a20d6e12be75a438d631f84aa802e13f))

## [1.1.0](https://github.com/im-anishraj/arnio/compare/v1.0.2...v1.1.0) (2026-05-14)


### Features

* add data quality engine ([6053ab9](https://github.com/im-anishraj/arnio/commit/6053ab93fa29b706a20f5fd8d905f046fedb36c5))
* add data quality engine ([f8abb2f](https://github.com/im-anishraj/arnio/commit/f8abb2f8202e9d1fa394a2e1e97576f003d113b0))

## [1.0.2](https://github.com/im-anishraj/arnio/compare/v1.0.1...v1.0.2) (2026-05-10)


### Documentation

* add language identifiers to unlabeled fenced code blocks (MD040) ([21aad9c](https://github.com/im-anishraj/arnio/commit/21aad9c06e1440efa20d377f7842da6afa8d9095))
* completely redesign README with flagship-quality presentation ([252988a](https://github.com/im-anishraj/arnio/commit/252988a770a0600074734ed44b48e7cbd6763a66))
* completely redesign README with flagship-quality presentation ([5953eb4](https://github.com/im-anishraj/arnio/commit/5953eb4a567e9941a9a5ff3c4bc892a19605c737))

## [1.0.1](https://github.com/im-anishraj/arnio/compare/v1.0.0...v1.0.1) (2026-05-09)


### Documentation

* add architecture guide, reframe benchmarks, add social preview ([f91e69e](https://github.com/im-anishraj/arnio/commit/f91e69e7ffb89adcaa4ed64a5ddd4173e889c045))
* add architecture guide, reframe benchmarks, add social preview ([ab2ddba](https://github.com/im-anishraj/arnio/commit/ab2ddbaf422b582b5fc855df71906612936568e9))
* add comprehensive docstrings to all public Python functions ([3cbe1b3](https://github.com/im-anishraj/arnio/commit/3cbe1b35b95678ecc7aa267663dcd998dd74d0f2))
* duplicated code ([62401a1](https://github.com/im-anishraj/arnio/commit/62401a1418acb149b74697495467fd05e22fa14f))
* enforce conventional commits in contributor guidelines ([d98f6cf](https://github.com/im-anishraj/arnio/commit/d98f6cf208f8acc5d34dc0bee280f28a64cc1dbe))
* remove duplicated code ([0e215f9](https://github.com/im-anishraj/arnio/commit/0e215f9080abbe77183f51a9a1b07e90d60bc54f))

## [Unreleased]
### Fixed
- Fixed type consistency check in Column (#52)

## [1.0.0] - 2026-05-08
### Added
- **Cross-Platform Wheels**: Full `cibuildwheel` automation delivering pre-compiled native wheels for Windows, Linux, and macOS (Intel & Apple Silicon).
- **Google Colab Compatibility**: Linux wheels are now fully `manylinux` compliant, allowing `pip install arnio` to work out-of-the-box on Colab and Ubuntu.
- **Production-Grade Packaging**: Resolved `ModuleNotFoundError` by removing double-nesting issues in `scikit-build-core` config.
- **CI/CD Excellence**: Fully automated PyPI publishing pipeline via Trusted Publishing with integrated source distributions (`sdist`).
- **Stable API**: Officially marked `arnio` as stable for production workloads with "Development Status :: 5 - Production/Stable".

### Fixed
- Migrated from `FetchContent` to `find_package(pybind11)` for faster, offline, and more robust cross-platform builds.
- Refactored `cibuildwheel` configuration entirely into `pyproject.toml` for standard and declarative packaging.

## [0.1.3] - 2026-05-06
### Fixed
- `normalize_case()` now accepts `case_type` kwarg as documented in README
  (previously accepted `case=`, causing TypeError for all README users)
- `to_pandas()` completely rewritten using zero-copy NumPy buffer interface —
  eliminates O(rows × cols) pybind11 boundary crossings, restoring actual 
  performance advantage over pandas
- `from_pandas()` implemented with correct null handling and round-trip fidelity

### Added
- `ar.register_step(name, fn)` — register pure-Python pipeline steps without C++
- `arnio.exceptions` module with `ArnioError`, `UnknownStepError`, `CsvReadError`, 
  `TypeCastError` — replaces opaque C++ errors with actionable messages
- `arnio.__version__` now available programmatically
- `benchmarks/generate_data.py` — deterministic 1M row test dataset generator
- `benchmarks/benchmark_vs_pandas.py` — reproducible end-to-end benchmark

### Fixed (Internal)
- CI now verifies compilation on Ubuntu and Windows across Python 3.9–3.12

## [0.1.2] - 2026-05-03
### Fixed
- Stability improvements and initial PyPI release
